# imports internos

# imports externos

MENU_PRINCIPAL_STR: str = """
Bem vindo ao Quantium Bank!

[1] Fazer login
[2] Registrar-se

[0] Sair

Opção: """

def menu_principal() -> str:
    """Retorna a entrada entregue pelo usuário após exibir o texto de `MENU_PRINCIPAL_STR`"""
    user_input: str = input(MENU_PRINCIPAL_STR)
    return user_input

MENU_LOGADO_STR: str = """
Olá %s, seja bem vindo!

Seu saldo atual é de %s

[1] Depositar
[2] Sacar
[3] Transferir
[4] Fazer logout

[0] Sair

Opção: """

def menu_logado(nome: str, saldo: str) -> str:
    """Retorna a entrada entregue pelo usuário após exibir o texto de `MENU_LOGADO_STR`"""
    user_input: str = input(MENU_LOGADO_STR % (nome, saldo))
    return user_input
