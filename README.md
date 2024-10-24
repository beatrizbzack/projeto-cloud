# 🎯 Projeto de API RESTful com Scraping de Dados

**Desenvolvido por: Beatriz Borges Zackiewicz**  

![API Banner](./assets/banner.png)  
<!-- Adicione uma imagem representativa do projeto -->

---

## 📖 Visão Geral

Este projeto envolve a criação de uma **API RESTful** para fornecer dados obtidos via **scraping**. A aplicação foi desenvolvida utilizando **FastAPI** e utiliza **MongoDB** como base de dados. Toda a infraestrutura está conteinerizada com **Docker**, permitindo uma fácil replicação do ambiente.

- **Frameworks**: FastAPI, Pydantic
- **Banco de Dados**: MongoDB
- **Scraping**: BeautifulSoup, Requests
- **Deploy**: Docker, Docker Hub

---

## 📚 Documentação Completa

A documentação oficial está hospedada no **GitHub Pages**, gerada automaticamente pelo **MkDocs**. Acesse o link abaixo para visualizar a versão completa:

[📄 Documentação Oficial do Projeto](https://seu-usuario.github.io/seu-projeto)

---

## 📂 Estrutura do Projeto

```bash
.
├── app/
│   ├── main.py                # Arquivo principal da API
│   ├── scraping.py            # Função de scraping de dados
│   ├── models.py              # Modelos de dados (Pydantic)
│   ├── routers.py             # Definição das rotas
│   └── utils.py               # Funções auxiliares
├── docker-compose.yaml        # Arquivo Docker Compose
├── Dockerfile                 # Dockerfile para a API
└── README.md                  # Este documento
