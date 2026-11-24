# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2026-11-24

### Adicionado
- Estrutura completa do pacote `quantium_bank` seguindo o padrão **MVC** (`model`, `view`, `controller`), ponto de entrada em `__main__.py` e configurações centralizadas em `config.py`.
- Camada de persistência em **SQLite** (`model/database.py` e `model/banco.py`) com ativação de chaves estrangeiras (`PRAGMA foreign_keys = ON`), criação automática das tabelas `usuarios` e `transacoes` e suporte a carga de usuários mock (`USUARIOS_MOCK`).
- Entidade de domínio `Usuario` (`model/usuario.py`) com atualização automática de estado após operações financeiras.
- Objetos de valor e validadores (`model/validadores.py`):
  - `CPF`: sanitização e validação de 11 dígitos numéricos com formatação.
  - `Nome`: normalização e validação de nome completo (nome e ao menos um sobrenome).
  - `Senha`: validação de tamanho e caracteres permitidos, geração de hash com **PBKDF2-SHA256** + salt aleatório e verificação segura com `compare_digest`.
  - `Dinheiro`: conversão precisa via `Decimal` para centavos inteiros (`saldo_centavos` / `valor_centavos`) e formatação em `R$`.
- Controladores de autenticação (`controller/autenticacao.py`) para login e registro de novos usuários.
- Controladores de operações bancárias (`controller/acoes.py`) para depósito, saque e transferência atômica entre contas por CPF.
- Interface CLI no terminal (`view/menus.py`, `view/telas.py`, `view/terminal.py`) com menus interativos, entrada oculta de senha via `getpass` e feedback colorido para informações, alertas e confirmações.
