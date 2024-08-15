# Mindtech Newsletter

Pprojeto web para gerenciar uma newsletter, permitindo aos usuários se inscrever e remover seus emails do banco de dados. A aplicação é construída com Python e Flask e utiliza um banco de dados SQLite.

## Pré-requisitos

- **Python 3.7+**: Pode baixar a versão mais recente do [site oficial do Python](https://www.python.org/downloads/).

## Instalação

### 1. Clonar o Repositório

Clone o repositório abaixo usando o comando:

```bash
git clone https://github.com/Ark4nJos/mindtech-newslatter.git
cd mindtech-newsletter
```

### 2. Criar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**: 
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**: 
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

Instale todas as bibliotecas usando o comando abaixo:

```bash
pip install -r requirements.txt
```

### 4. Criar o Banco de Dados

Execute o script `criar_db.py` para criar o banco de dados:

```bash
python src/db/criar_db.py
```

Este script irá criar um arquivo `database.db`.

## Executando o Servidor

Após a instalação e configuração,pode iniciar o servidor Flask executando o seguinte comando:

```bash
python src/app.py
```

O servidor estará disponível em `http://127.0.0.1:5000/`. Abra o navegador e  acesse a aplicação.


## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para o desenvolvimento da aplicação.
- **Flask**: Framework web utilizado para construir a aplicação.
- **SQLite**: Sistema de gerenciamento de banco de dados leve usado para armazenar os e-mails.