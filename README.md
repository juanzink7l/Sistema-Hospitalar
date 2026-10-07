# 🏥 Sistema Hospitalar

Sistema web para gerenciamento de pacientes e processos de triagem hospitalar, desenvolvido com Django.

O projeto tem como objetivo facilitar o cadastro, consulta e gerenciamento de pacientes, oferecendo uma interface simples e intuitiva para utilização durante o processo de triagem.

---

## 📋 Sobre o projeto

O **Sistema Hospitalar** é uma aplicação web desenvolvida em Python utilizando o framework Django.

O sistema permite que usuários autenticados realizem o gerenciamento de pacientes dentro de um ambiente de triagem.

Entre as funcionalidades atuais estão:

- 👤 Cadastro de pacientes
- 📋 Listagem de pacientes
- ✏️ Alteração dos dados dos pacientes
- 🗑️ Exclusão de pacientes
- 🩺 Registro dos sintomas
- 🔐 Sistema de autenticação
- 📅 Registro da data de nascimento
- 🆔 Identificação única dos pacientes
- 🖥️ Interface web responsiva
- 🎨 Interface com tema moderno e escuro

---

## 🚀 Tecnologias utilizadas

Este projeto foi desenvolvido utilizando:

- 🐍 **Python**
- 🌐 **Django**
- 🗄️ **SQLite**
- 🎨 **HTML5**
- 🎨 **CSS3**
- 🅱️ **Bootstrap**

---

## 📁 Estrutura do projeto

Sistema-Hospital/ │ ├── apps/ │ └── triagem/ │ ├── migrations/ │ ├── templates/ │ ├── models.py │ ├── views.py │ ├── urls.py │ └── ... │ ├── config/ │ ├── settings.py │ ├── urls.py │ ├── asgi.py │ └── wsgi.py │ ├── db_sus.db ├── manage.py └── README.md


---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

git clone https://github.com/juanzink7l/Sistema-Hospital.git


Entre na pasta:

cd Sistema-Hospital


---

### 2. Crie um ambiente virtual

Windows:

python -m venv venv


Linux/macOS:

python3 -m venv venv


---

### 3. Ative o ambiente virtual

Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate


---

### 4. Instale as dependências

pip install django


> Caso o projeto possua um arquivo `requirements.txt`, prefira utilizar:

pip install -r requirements.txt


---

### 5. Execute as migrations

python manage.py makemigrations


Depois:

python manage.py migrate


---

### 6. Crie um usuário administrador

python manage.py createsuperuser


Preencha:

Username: Email: Password:


---

### 7. Execute o servidor

python manage.py runserver


O sistema ficará disponível em:

http://127.0.0.1:8000/


---

## 👥 Gerenciamento de pacientes

O sistema possui um módulo dedicado à triagem e gerenciamento de pacientes.

Cada paciente possui informações como:

Campo	Descrição
Código	Identificador único
Nome	Nome completo do paciente
CPF	Documento de identificação
Data de nascimento	Data de nascimento
Sintomas	Sintomas relatados pelo paciente
🩺 Triagem
A área de triagem apresenta os pacientes cadastrados de forma visual, permitindo ao usuário visualizar rapidamente as informações principais.

Os pacientes são apresentados em cards contendo:

Código do paciente
Nome
CPF
Data de nascimento
Sintomas
Status do paciente
Opção para alterar dados
Opção para excluir o paciente
✏️ Alteração de pacientes
Os dados cadastrados podem ser alterados posteriormente através da opção:

Alterar
Isso permite corrigir ou atualizar informações do paciente sem precisar realizar um novo cadastro.

🗑️ Exclusão de pacientes
Também é possível remover pacientes através da opção:

Excluir
O sistema solicita uma confirmação antes da exclusão para evitar remoções acidentais.

🔐 Autenticação
O sistema utiliza o sistema de autenticação do Django para controlar o acesso às áreas protegidas da aplicação.

Usuários não autenticados não devem ter acesso às funcionalidades restritas do sistema.

🗄️ Banco de dados
Atualmente, o projeto utiliza SQLite.

O banco utilizado durante o desenvolvimento está localizado em:

db_sus.db
As alterações na estrutura do banco devem ser realizadas através das migrations do Django:

python manage.py makemigrations
python manage.py migrate
🛠️ Desenvolvimento
Para executar o projeto durante o desenvolvimento:

python manage.py runserver
Após iniciar o servidor, acesse:

http://127.0.0.1:8000/
