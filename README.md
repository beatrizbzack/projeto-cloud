# 🎯 Projeto de API RESTful com Scraping de Dados - Fatos Aleatórios

**Desenvolvido por: Beatriz Borges Zackiewicz**  

![API Banner](./assets/ilustracao-projeto.png)  
<!-- Adicione uma imagem representativa do projeto -->

---

## 📖 Visão Geral

Este projeto envolve a criação de uma **API RESTful** para fornecer dados obtidos via **scraping**. A aplicação foi desenvolvida utilizando **FastAPI** e utiliza **POSTGRES** como base de dados. Toda a infraestrutura está conteinerizada com **Docker**, permitindo uma fácil replicação do ambiente.

- **Frameworks**: FastAPI, Pydantic
- **Banco de Dados**: Postgres
- **Scraping**: Requests
- **Deploy**: Docker, Docker Hub

---

## 📚 Documentação Completa

A documentação oficial está hospedada no **GitHub Pages**, gerada automaticamente pelo **MkDocs**. Acesse o link abaixo para visualizar a versão completa:

[📄 Documentação Oficial do Projeto](https://seu-usuario.github.io/seu-projeto)

---

## 📂 Estrutura do Projeto

```bash
.
├── app
│   ├── __pycache__
│   │   └── __init__.py
│   ├── auth.py
│   ├── db.py
│   ├── Dockerfile
│   ├── exec.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── routes.py
│   ├── schemas.py
│   ├── scraping.py
│   ├── services.py
├── assets
│   └── ilustracao-projeto.png
├── db
│   └── 01_init.sql
├── tests
│   └── test_auth.py
├── venv
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md

