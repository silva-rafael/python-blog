# Blog Simples em Django

Bem-vindo ao meu projeto de aprendizado: um blog simples construído utilizando o framework Django. Este projeto foi desenvolvido com o objetivo de explorar conceitos fundamentais de Django e entender como criar, configurar e gerenciar uma aplicação web básica.

---

## Índice

- [Descrição do Projeto](#descri%C3%A7%C3%A3o-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos](#requisitos)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Licença](#licen%C3%A7a)

---

## Descrição do Projeto

Este projeto é um blog básico onde os usuários podem:

- Visualizar postagens.
- Criar, editar e deletar postagens (apenas para administradores).
- Navegar entre as postagens listadas por data de publicação.

O objetivo é compreender o fluxo de desenvolvimento de aplicações Django, como trabalhar com models, views e templates, e explorar o admin do Django.

---

## Funcionalidades

- Listagem de postagens.
- Visualização de detalhes de uma postagem.
- Interface administrativa para gerenciar postagens.

---

## Tecnologias Utilizadas

- **Python** (versão 3.8 ou superior)
- **Django** (versão 4.2 ou superior)
- **SQLite** (banco de dados padrão do Django)
- HTML, CSS (Bootstrap para estilização básica)

---

## Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados na sua máquina:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acesse o blog no navegador:
   ```
   http://127.0.0.1:8000/
   ```

---

## Uso

1. Acesse o painel administrativo em `http://127.0.0.1:8000/admin/` para gerenciar postagens.
2. Crie novas postagens ou edite as existentes.
3. Navegue pelo blog e visualize as postagens criadas.

---

## Estrutura do Projeto

```plaintext
seu-repositorio/
├── blog/                 # Aplicação principal
│   ├── migrations/       # Arquivos de migração do banco de dados
│   ├── templates/        # Templates HTML do projeto
│   ├── admin.py          # Configuração do painel administrativo
│   ├── apps.py           # Configuração da aplicação
│   ├── models.py         # Modelos de dados
│   ├── urls.py           # Rotas da aplicação
│   ├── views.py          # Lógica das páginas
├── projeto_django/       # Configuração do projeto Django
│   ├── settings.py       # Configurações do projeto
│   ├── urls.py           # Rotas principais
│   ├── wsgi.py           # Configuração WSGI
├── manage.py             # Comando de gerenciamento do Django
├── requirements.txt      # Dependências do projeto
```

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests no [repositório no GitHub](https://github.com/seu-usuario/seu-repositorio).

---

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

