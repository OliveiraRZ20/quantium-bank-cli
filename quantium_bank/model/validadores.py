# imports internos
from quantium_bank.config import REGEX_SENHA, REGEX_NOME

# imports externos
from hashlib import pbkdf2_hmac
from hmac import compare_digest
from os import urandom
from decimal import Decimal, InvalidOperation

class CPF:
    def __init__(self, valor: str) -> None:
        self.__valor: str = valor.strip().replace(".", "").replace("-", "")
        if not self.__valor.isdigit():
            raise ValueError("O CPF deve conter somente dígitos")
        if len(self.__valor) != 11:
            raise ValueError("O CPF deve conter exatamente 11 dígitos")

    @property
    def valor(self) -> str:
        return self.__valor

    def __str__(self) -> str:
        v: str = self.__valor
        return f"{v[:3]}.{v[3:6]}.{v[6:9]}-{v[9:]}"

    def __repr__(self) -> str:
        return f"CPF('{self.__valor}')"

class Senha:
    def __init__(self, valor: str) -> None:
        self.__valor: str = valor
        if len(self.__valor) < 5:
            raise ValueError("A senha não pode conter menos que 5 caracteres.")
        if len(self.__valor) > 32:
            raise ValueError("A senha não pode conter mais que 32 caracteres.")
        if " " in self.__valor:
            raise ValueError("A senha não pode conter espaços em branco")
        if not REGEX_SENHA.fullmatch(self.__valor):
            raise ValueError("A senha deve conter apenas letras, números ou os símbolos !@#$%.")

    def gerar_hash(self) -> str:
        """Gera salt aleatório + hash PBKDF2-SHA256 no formato 'salt_hex:hash_hex'."""
        salt: bytes = urandom(16)
        hash_bytes: bytes = pbkdf2_hmac(
            hash_name="sha256",
            password=self.__valor.encode("utf-8"),
            salt=salt,
            iterations=100_000,
        )
        return f"{salt.hex()}:{hash_bytes.hex()}"

    @staticmethod
    def conferir_hash(senha_plana: str, hash_salvo: str) -> bool:
        """Extrai o salt do banco, recalcula o PBKDF2 e compara de forma segura."""
        try:
            salt_hex, hash_hex = hash_salvo.split(":")
            salt: bytes = bytes.fromhex(salt_hex)
            novo_hash: bytes = pbkdf2_hmac(
                hash_name="sha256",
                password=senha_plana.encode("utf-8"),
                salt=salt,
                iterations=100_000,
            )
            return compare_digest(novo_hash.hex(), hash_hex)
        except ValueError:
            return False

    def __str__(self) -> str:
        return "*" * len(self.__valor)

    def __repr__(self) -> str:
        return f"Senha('{'*' * len(self.__valor)}')"

class Nome:
    def __init__(self, valor: str) -> None:
        self.__valor: str = " ".join(valor.strip().split()).title()
        if " " not in self.__valor:
            raise ValueError("O nome deve conter pelo menos um sobrenome.")
        if not REGEX_NOME.fullmatch(self.__valor):
            raise ValueError("O nome deve conter apenas letras e pelo menos um sobrenome.")

    @property
    def valor(self) -> str:
        return self.__valor

    def __str__(self) -> str:
        return self.__valor

    def __repr__(self) -> str:
        return f"Nome('{self.__valor}')"

from decimal import Decimal, InvalidOperation


class Dinheiro:
    def __init__(self, valor_reais: str | float | int) -> None:
        try:
            texto: str = str(valor_reais).strip().replace(",", ".")
            valor_decimal: Decimal = Decimal(texto)
        except InvalidOperation:
            raise ValueError("Valor monetário inválido.")

        if not valor_decimal.is_finite():
            raise ValueError("Valor monetário inválido.")

        if valor_decimal <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        expoente = valor_decimal.as_tuple().exponent
        if isinstance(expoente, int) and expoente < -2:
            raise ValueError("O valor não pode ter mais que 2 casas decimais.")

        self.__centavos: int = int(valor_decimal * 100)

    @property
    def centavos(self) -> int:
        return self.__centavos

    @staticmethod
    def formatar(centavos: int) -> str:
        """Formata um inteiro em centavos para exibição (ex: 15050 -> 'R$ 150,50')."""
        reais: float = centavos / 100
        return f"R$ {reais:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def __str__(self) -> str:
        return self.formatar(self.__centavos)

    def __repr__(self) -> str:
        return f"Dinheiro({self.__centavos})"
