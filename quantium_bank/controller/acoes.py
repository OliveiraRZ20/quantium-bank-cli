# imports internos
from quantium_bank.model.usuario import Usuario
from quantium_bank.model.banco import Banco
from quantium_bank.view.telas import solicitar_deposito, solicitar_saque, solicitar_transferencia
from quantium_bank.model.validadores import Dinheiro, CPF


# imports externos

def depositar(usuario: Usuario) -> None:
    valor_reais_raw: str = solicitar_deposito()

    valor_reais: Dinheiro = Dinheiro(valor_reais_raw)
    usuario.depositar(valor_reais)

def sacar(usuario: Usuario) -> None:
    valor_reais_raw: str = solicitar_saque()

    valor_reais: Dinheiro = Dinheiro(valor_reais_raw)
    usuario.sacar(valor_reais)

def transferir(usuario: Usuario, banco: Banco) -> None:
    cpf_destino_raw, valor_reais_raw = solicitar_transferencia()

    cpf_destino: CPF = CPF(cpf_destino_raw)
    usuario_destino: dict | None = banco.buscar_usuario_por_cpf(cpf_destino.valor)
    if not usuario_destino:
        raise ValueError("CPF destino inválido.")

    valor_reais: Dinheiro = Dinheiro(valor_reais_raw)
    usuario.transferir(cpf_destino, valor_reais)

