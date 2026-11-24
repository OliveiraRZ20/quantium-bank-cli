# imports internos
from quantium_bank.config import DB_PATH, USUARIOS_MOCK

# imports externos
from sqlite3 import connect, Row, Connection
from pathlib import Path


def conectar(db_path: Path = DB_PATH) -> Connection:
    """Retorna um objeto `Connection` do `sqlite3` realizando a abertura de conexão com o banco de dados:"""
    # funcionamento do sqlite se baseia primeiro em uma conexão de banco de dados
    conn: Connection = connect(db_path)
    # obs 01: isso faz o resultados virem como dicionários
    conn.row_factory = Row
    # obs 02: isso ativa a validação de FKs
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def criar_tabelas(conn: Connection) -> None:
    sql_script: str = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        senha_hash TEXT NOT NULL,
        -- saldo_centavos como integer para evitar erros de float e check para saldo negativo
        saldo_centavos INTEGER NOT NULL DEFAULT 0 CHECK (saldo_centavos >= 0),
        criado_em TEXT DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_origem_id INTEGER,
        usuario_destino_id INTEGER,
        tipo TEXT NOT NULL CHECK (tipo IN ('DEPOSITO', 'SAQUE', 'TRANSFERENCIA')),
        valor_centavos INTEGER NOT NULL CHECK (valor_centavos > 0),
        data_hora TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_origem_id) REFERENCES usuarios(id),
        FOREIGN KEY (usuario_destino_id) REFERENCES usuarios(id)
    );
    """
    conn.executescript(sql_script)
    conn.commit()

def criar_usuarios_mock(conn: Connection, usuarios: list[tuple[str, str, str]] = USUARIOS_MOCK) -> bool:
    """Cria vários usuários na tabela usuarios de uma vez só utilizando uma lista de tuplas contendo as informações dos mesmos."""
    with conn:
        cursor = conn.cursor()
        sql_query: str = "INSERT OR IGNORE INTO usuarios (nome, cpf, senha_hash) VALUES (?, ?, ?)"
        cursor.executemany(sql_query, usuarios)
        return cursor.rowcount > 0

def inicializar_database(utilizar_dados_mock: bool = False) -> Connection:
    conn: Connection = conectar()
    criar_tabelas(conn)
    if utilizar_dados_mock is True:
        criar_usuarios_mock(conn)
    return conn

if __name__ == "__main__":
    inicializar_database(utilizar_dados_mock=True)
