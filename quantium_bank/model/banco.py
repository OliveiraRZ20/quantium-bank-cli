# imports internos

# imports externos
from sqlite3 import Connection, IntegrityError

class Banco:
    def __init__(self, conn: Connection) -> None:
        self.conn: Connection = conn

    def criar_usuario(self, nome: str, cpf: str, senha_hash: str) -> bool:
        """Cria um usuário na tabela usuarios utilizando como input o nome, cpf e senha_hash."""
        with self.conn:
            cursor = self.conn.cursor()
            try:
                sql_query: str = "INSERT INTO usuarios (nome, cpf, senha_hash) VALUES (?, ?, ?)"
                cursor.execute(sql_query, (nome, cpf, senha_hash))
                return cursor.rowcount > 0
            except IntegrityError as e:
                raise ValueError(f"CPF '{cpf}' já está cadastrado!") from e

    def sacar(self, usuario_id: int, valor_centavos: int) -> bool:
        if valor_centavos <= 0:
            raise ValueError("O valor inserido para sacar deve ser maior que zero.")

        with self.conn:
            cursor = self.conn.cursor()

            sql_query: str = "SELECT saldo_centavos FROM usuarios WHERE id = ?"
            cursor.execute(sql_query, (usuario_id,))
            resultado = cursor.fetchone()
            if not resultado:
                raise ValueError("Usuário não encontrado.")

            saldo_centavos: int = resultado["saldo_centavos"]
            if saldo_centavos - valor_centavos < 0:
                raise ValueError("Saldo insuficiente para o saque")

            sql_query: str = "UPDATE usuarios SET saldo_centavos = saldo_centavos - ? WHERE id = ?"
            cursor.execute(sql_query, (valor_centavos, usuario_id))

            sql_query: str = """
            INSERT INTO transacoes (usuario_origem_id, usuario_destino_id, tipo, valor_centavos)
            VALUES (?, NULL, 'SAQUE', ?)
            """
            cursor.execute(sql_query, (usuario_id, valor_centavos))
            return cursor.rowcount > 0

    def depositar(self, usuario_id: int, valor_centavos: int) -> bool:
        if valor_centavos <= 0:
            raise ValueError("O valor inserido para depositar deve ser maior que zero")

        with self.conn:
            cursor = self.conn.cursor()

            sql_query: str = "UPDATE usuarios SET saldo_centavos = saldo_centavos + ? WHERE id = ?"
            cursor.execute(sql_query, (valor_centavos, usuario_id))
            if cursor.rowcount == 0:
                raise ValueError("Usuário não encontrado")

            sql_query: str = """
            INSERT INTO transacoes (usuario_origem_id, usuario_destino_id, tipo, valor_centavos)
            VALUES (NULL, ?, 'DEPOSITO', ?)
            """
            cursor.execute(sql_query, (usuario_id, valor_centavos))
            return cursor.rowcount > 0

    def transferir(self, usuario_origem_id: int, cpf_destino: str, valor_centavos: int) -> bool:
        if valor_centavos <= 0:
            raise ValueError("O valor inserido para transferir deve ser maior que zero.")

        with self.conn:
            cursor = self.conn.cursor()

            # 01. Valida que usuário origem existe
            # 03. Valida que usuário origem tem saldo para a transferência proposta
            sql_query: str = "SELECT saldo_centavos FROM usuarios WHERE id = ?"
            cursor.execute(sql_query, (usuario_origem_id,))
            resultado = cursor.fetchone()
            if not resultado:
                raise ValueError("Usuário origem não encontrado")

            saldo_centavos: int = resultado["saldo_centavos"]
            if saldo_centavos - valor_centavos < 0:
                raise ValueError("Saldo insuficiente para a transferência")

            # 02. Valida que usuário destino existe
            sql_query: str = "SELECT id FROM usuarios WHERE cpf = ?"
            cursor.execute(sql_query, (cpf_destino,))
            resultado = cursor.fetchone()
            if not resultado:
                raise ValueError("Usuário destino não encontrado")
            usuario_destino_id: int = resultado["id"]

            if usuario_origem_id == usuario_destino_id:
                raise ValueError("Não é possível transferir para a própria conta.")

            # 04. Transfere o dinheiro
            # 04.1 Diminui o saldo da conta de origem
            sql_query: str = "UPDATE usuarios SET saldo_centavos = saldo_centavos - ? WHERE id = ?"
            cursor.execute(sql_query, (valor_centavos, usuario_origem_id))

            # 04.2 Aumenta o saldo da conta de destino
            sql_query: str = "UPDATE usuarios SET saldo_centavos = saldo_centavos + ? WHERE id = ?"
            cursor.execute(sql_query, (valor_centavos, usuario_destino_id))

            # 04.3 Registra a transação na tabela transacoes
            sql_query: str = """
            INSERT INTO transacoes (usuario_origem_id, usuario_destino_id, tipo, valor_centavos)
            VALUES (?, ?, 'TRANSFERENCIA', ?)
            """
            cursor.execute(sql_query, (usuario_origem_id, usuario_destino_id, valor_centavos))
            return cursor.rowcount > 0

    def buscar_usuario_por_cpf(self, cpf: str) -> dict | None:
        """Retorna um dicionário Python contendo todas as informações de um usuário na tabela usuarios."""
        sql_query: str = "SELECT id, nome, cpf, senha_hash, saldo_centavos, criado_em FROM usuarios WHERE cpf = ?"
        cursor = self.conn.cursor()
        cursor.execute(sql_query, (cpf,))
        resultado = cursor.fetchone()
        return dict(resultado) if resultado else None
