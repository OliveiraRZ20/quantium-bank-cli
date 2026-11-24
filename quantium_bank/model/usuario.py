# imports internos
from quantium_bank.model.banco import Banco
from quantium_bank.model.validadores import Dinheiro, CPF

# imports externos

class Usuario:
    def __init__(self, dados: dict, banco: Banco) -> None:
        self.__dados: dict = dados
        self.__banco: Banco = banco

    @property
    def dados(self) -> dict[str, str]:
        return self.__dados

    def __atualizar_dados(self) -> None:
        atualizado = self.__banco.buscar_usuario_por_cpf(self.__dados["cpf"])
        if atualizado:
            self.__dados = atualizado

    def depositar(self, valor: Dinheiro) -> None:
        self.__banco.depositar(self.__dados["id"], valor.centavos)
        self.__atualizar_dados()

    def sacar(self, valor: Dinheiro) -> None:
        if valor.centavos > self.__dados["saldo_centavos"]:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.__banco.sacar(self.__dados["id"], valor.centavos)
        self.__atualizar_dados()

    def transferir(self, destino: CPF, valor: Dinheiro) -> None:
        if destino.valor == self.__dados["cpf"]:
            raise ValueError("Não é possível transferir para a própria conta.")
        if valor.centavos > self.__dados["saldo_centavos"]:
            raise ValueError("Saldo insuficiente para realizar a transferência.")
        self.__banco.transferir(self.__dados["id"], destino.valor, valor.centavos)
        self.__atualizar_dados()

    def __str__(self) -> str:
        dados_publicos = {k: v for k, v in self.__dados.items() if k != "senha_hash"}
        return " | ".join(f"{chave}: {valor}" for chave, valor in dados_publicos.items())

    def __repr__(self) -> str:
        return f"Usuario(id={self.__dados.get('id')}, nome='{self.__dados.get('nome')}', cpf='{self.__dados.get('cpf')}')"
