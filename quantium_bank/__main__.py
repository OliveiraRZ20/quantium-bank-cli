# imports internos
from quantium_bank.controller.autenticacao import fazer_login, registrar_se
from quantium_bank.controller.acoes import depositar, sacar, transferir
from quantium_bank.model.database import inicializar_database
from quantium_bank.model.banco import Banco
from quantium_bank.model.usuario import Usuario
from quantium_bank.model.validadores import Dinheiro
from quantium_bank.view.terminal import cls, pause, informar, alertar, confirmar
from quantium_bank.view.menus import menu_principal, menu_logado

# imports externos
from sqlite3 import Connection
from sys import exit


def main() -> None:
    cls()
    conn: Connection = inicializar_database()
    banco: Banco = Banco(conn)
    usuario_logado: Usuario | None = None
    while True:
        while not usuario_logado:
            cls()
            match menu_principal():
                case "1":
                    try:
                        usuario_logado: Usuario | None = fazer_login(banco)
                        if not usuario_logado:
                            alertar("Credenciais inválidas!")
                        else:
                            confirmar("Usuário autenticado com sucesso!")
                    except ValueError as e:
                        alertar(str(e))
                case "2":
                    try:
                        usuario_logado: Usuario | None = registrar_se(banco)
                        if usuario_logado is not None:
                            confirmar("Usuário registrado com sucesso!")
                    except ValueError as e:
                        alertar(str(e))
                case "0":
                    confirmar("Execução finalizada com sucesso! até mais tarde.")
                    exit(0)
                case _:
                    alertar("Opção inválida, tente novamente!")
            pause()
        while usuario_logado != None:
            cls()
            match menu_logado(usuario_logado.dados["nome"], Dinheiro.formatar(int(usuario_logado.dados["saldo_centavos"]))):
                case "1":
                    depositar(usuario_logado)
                case "2":
                    sacar(usuario_logado)
                case "3":
                    transferir(usuario_logado, banco)
                case "4":
                    usuario_logado: Usuario | None = None
                    confirmar("Logou realizado com sucesso!")
                case "0":
                    confirmar("Execução finalizada com sucesso! até mais tarde.")
                    exit(0)
                case _:
                    alertar("Opção inválida, tente novamente!")
            pause()


if __name__ == "__main__":
    main()
