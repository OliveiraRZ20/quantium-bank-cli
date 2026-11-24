# imports internos
from quantium_bank.view.telas import solicitar_login, solicitar_registro
from quantium_bank.model.validadores import CPF, Senha, Nome
from quantium_bank.model.banco import Banco
from quantium_bank.model.usuario import Usuario

# imports externos

def fazer_login(banco: Banco) -> Usuario | None:
    cpf_raw, senha_raw = solicitar_login()

    cpf = CPF(cpf_raw)

    usuario_dados: dict | None = banco.buscar_usuario_por_cpf(cpf.valor)
    if not usuario_dados:
        return None

    senha_hash: str = usuario_dados["senha_hash"]
    match Senha.conferir_hash(senha_raw, senha_hash):
        case True:
            return Usuario(usuario_dados, banco)
        case False:
            return None


def registrar_se(banco: Banco) -> Usuario | None:
    nome_raw, cpf_raw, senha_raw = solicitar_registro()

    nome = Nome(nome_raw)
    cpf = CPF(cpf_raw)
    senha = Senha(senha_raw)

    banco.criar_usuario(nome.valor, cpf.valor, senha.gerar_hash())
    usuario_dados: dict | None = banco.buscar_usuario_por_cpf(cpf.valor)
    if not usuario_dados:
        return None
    return Usuario(usuario_dados, banco)
