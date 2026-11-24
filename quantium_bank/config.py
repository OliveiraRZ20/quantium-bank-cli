# imports internos

# imports externos
from pathlib import Path
from re import compile, Pattern


APP_NAME: str = "Quantium Bank"
APP_VERSION: str = "1.0.0"

# Caminhos

PACKAGE_DIR: Path = Path(__file__).resolve().parent

MODEL_DIR: Path = PACKAGE_DIR / "model"
VIEW_DIR: Path = PACKAGE_DIR / "view"
CONTROLLER_DIR: Path = PACKAGE_DIR / "controller"

STORAGE_DIR: Path = MODEL_DIR / "storage"
DB_PATH: Path = STORAGE_DIR / "banco.db"

REGEX_SENHA: Pattern = compile(r"^[a-zA-Z0-9!@#$%]+$")
REGEX_NOME: Pattern = compile(r"^[a-zA-ZÀ-ÿ]+(?: [a-zA-ZÀ-ÿ]+)+$")

USUARIOS_MOCK: list[tuple[str, str, str]] = [
    ("Ana Clara Souza", "10482930112", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Bruno Henrique Lima", "23948102934", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Camila Ferreira Costa", "38492019283", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Daniel Oliveira Santos", "49201928374", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Eduarda Martins Silva", "51029384756", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Felipe Rocha Almeida", "62938475610", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Gabriela Mendes Dias", "73849201928", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Henrique Barbosa Nunes", "84920192837", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Isabela Gomes Pereira", "95019283746", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("João Pedro Carvalho", "11223344550", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Karina Ribeiro Castro", "22334455661", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Lucas Fernandes Araujo", "33445566772", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Mariana Cardoso Pinto", "44556677883", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Nicolas Teixeira Moura", "55667788994", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Olivia Monteiro Vieira", "66778899005", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Paulo Victor Nascimento", "77889900116", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Quezia Moreira Freitas", "88990011227", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Rafael Correia Lopes", "99001122338", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Sabrina Duarte Cavalcanti", "10293847501", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Thiago Borges Ramos", "20394857612", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Ursula Farias Machado", "30495867123", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Vinicius Rezende Campos", "40596871234", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Yasmin Nogueira Azevedo", "50697812345", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Zeca Pagodinho da Silva", "60798123456", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Arthur Andrade Melo", "70891234567", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Beatriz Tavares Cunha", "80912345678", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Caio Cesar Mendes", "91023456789", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Debora Batista Santana", "12131415161", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Enzo Gabriel Brito", "23242526272", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Fernanda Vasconcelos", "34353637383", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Guilherme Peixoto Neves", "45464748494", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Helena Siqueira Barros", "56575859505", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Igor Miranda Pacheco", "67686960616", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Julia Fonseca Guimarães", "78797071727", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Kevin Morais Aguiar", "89808182838", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Larissa Coelho Vargas", "90919293949", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Matheus Paiva Amaral", "13579246801", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Natalia Xavier Rios", "24680135792", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Otavio Lemos Franco", "35791246803", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Patricia Queiroz Braga", "46802135794", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Renan Soares Figueredo", "57913246805", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Sofia Dantas Magalhães", "68024135796", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Tiago Medeiros Chaves", "79135246807", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Vanessa Pinheiro Sales", "80246135798", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Wagner Macedo Coutinho", "91357246809", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Xuxa Meneghel Torres", "14725836901", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Yuri Gagarin Silveira", "25836914702", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Zilda Arns Nogueira", "36914725803", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Alice Matos Ferraz", "47125836904", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
    ("Bernardo Cruz Leal", "58236914705", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
]

