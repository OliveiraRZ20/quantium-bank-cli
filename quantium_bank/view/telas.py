# imports internos
from quantium_bank.view.terminal import cls

# imports externos
from getpass import getpass


def solicitar_login() -> tuple[str, str]:
    """Retorna uma tupla de informações no formato (cpf, senha) que são solicitadas ao usuário com validações mínimas de formato"""
    cls()
    print("=" * 30)
    print("    QUANTIUM BANK - LOGIN")
    print("=" * 30)
    cpf: str = input("CPF (apenas números): ").strip().replace(".", "").replace("-", "")
    senha: str = getpass("Senha: ").strip()
    return (cpf, senha)

def solicitar_registro() -> tuple[str, str, str]:
    """Retorna uma tupla de informações no formato (nome, cpf, senha) que são solicitadas ao usuário com validações mínimas de formato"""
    cls()
    print("=" * 30)
    print("   QUANTIUM BANK - REGISTRO")
    print("=" * 30)
    nome: str = input("Nome Completo: ").strip().title()
    cpf: str = input("CPF (apenas números): ").strip().replace(".", "").replace("-", "")
    senha: str = getpass("Senha: ")
    return (nome, cpf, senha)

def solicitar_deposito() -> str:
    cls()
    print("=" * 30)
    print("   QUANTIUM BANK - DEPOSITO")
    print("=" * 30)
    valor_reais: str = input("Valor do depósito: ").strip()
    return valor_reais

def solicitar_saque() -> str:
    cls()
    print("=" * 30)
    print("   QUANTIUM BANK - SAQUE")
    print("=" * 30)
    valor_reais: str = input("Valor do saque: ").strip()
    return valor_reais

def solicitar_transferencia() -> tuple[str, str]:
    cls()
    print("=" * 30)
    print("   QUANTIUM BANK - TRANSFERÊNCIA")
    print("=" * 30)
    cpf_destino: str = input("CPF de destino: ").strip()
    valor_reais: str = input("Valor da transferência: ").strip()
    return (cpf_destino, valor_reais)
