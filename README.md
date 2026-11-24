# Quantium Bank

Sistema bancário em linha de comando (CLI) desenvolvido em **Python** com persistência em **SQLite**, estruturado no padrão arquitetural **MVC (Model-View-Controller)** para trabalho acadêmico de Modelagem de Software.

## Funcionalidades

- **Cadastro de usuários**: registro com validação de nome completo, CPF (11 dígitos) e senha (5 a 32 caracteres).
- **Autenticação segura**: login por CPF e senha utilizando hash **PBKDF2-SHA256** com salt aleatório de 16 bytes e comparação em tempo constante (`hmac.compare_digest`).
- **Depósito**: crédito em conta com registro de transação.
- **Saque**: débito com verificação de saldo disponível e registro de transação.
- **Transferência entre contas**: movimentação atômica entre usuários por CPF de destino, com validação de saldo, existência do destinatário e bloqueio de transferência para a própria conta.
- **Persistência e integridade**: valores monetários armazenados em centavos (`INTEGER`) para evitar imprecisões de ponto flutuante, além de chaves estrangeiras e restrições `CHECK` no SQLite.

## Arquitetura e Estrutura do Projeto

```text
refazendo-a3/
├── quantium_bank/
│   ├── __init__.py
│   ├── __main__.py              # Ponto de entrada e loop principal da aplicação
│   ├── config.py                # Configurações, caminhos, regex e dados mock
│   ├── controller/
│   │   ├── acoes.py             # Fluxos de depósito, saque e transferência
│   │   └── autenticacao.py      # Fluxos de login e registro
│   ├── model/
│   │   ├── banco.py             # Operações transacionais e consultas no SQLite
│   │   ├── database.py          # Conexão, criação de tabelas e carga de mocks
│   │   ├── usuario.py           # Entidade Usuario e regras de sessão
│   │   ├── validadores.py       # Value Objects (CPF, Senha, Nome, Dinheiro)
│   │   └── storage/
│   │       └── banco.db         # Banco de dados SQLite
│   └── view/
│       ├── menus.py             # Menus principal e autenticado
│       ├── telas.py             # Coleta de dados via terminal
│       └── terminal.py          # Utilitários de console (limpeza, pausa e mensagens)
├── old/                         # Protótipo inicial (notebook e script SQL)
├── CHANGELOG.md
└── README.md
```

## Modelo de Dados

O banco SQLite é composto por duas tabelas principais:

- **`usuarios`**: `id`, `nome`, `cpf` (`UNIQUE`), `senha_hash`, `saldo_centavos` (`>= 0`) e `criado_em`.
- **`transacoes`**: `id`, `usuario_origem_id` (FK), `usuario_destino_id` (FK), `tipo` (`DEPOSITO`, `SAQUE`, `TRANSFERENCIA`), `valor_centavos` (`> 0`) e `data_hora`.

## Pré-requisitos

- **Python 3.13+** (utiliza apenas a biblioteca padrão, sem dependências externas).
- Sistema operacional **Windows** (os comandos de terminal `cls` e `pause` em `view/terminal.py` são nativos do Windows).

## Como Executar

A partir da raiz do repositório, execute o pacote como módulo:

```bash
python -m quantium_bank
```

Caso deseje inicializar o banco de dados manualmente com os usuários mock definidos em `config.py`:

```bash
python -m quantium_bank.model.database
```

## Licença

Projeto desenvolvido para fins acadêmicos.
