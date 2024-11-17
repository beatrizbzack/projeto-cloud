# 🎯 Projeto de API RESTful com Scraping de Dados - Fatos Aleatórios

**Desenvolvido por: Beatriz Borges Zackiewicz**  
**Docker Hub: https://hub.docker.com/r/beatrizbzack/projeto-cloud-app**

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

```markdown
## 📂 Estrutura do Projeto

```bash
.
├── app
│   ├── __pycache__
│   │   └── __init__.py
│   ├── auth.py
│   ├── db.py
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── routes.py
│   ├── schemas.py
│   ├── scraping.py
│   ├── services.py
├── assets
├── db
├── tests
│   ├── test_auth.py
│   ├── testar_api.py
│   ├── testar_registro.py
├── venv
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yml
├── lala.py
├── deployment.yml
├── postgres-deployment.yml
├── service.yml
└── README.md

```
--- 
## Endpoints da API
### **Registrar Usuário**

- **URL**: `/registrar`
- **Método**: `POST`
- **Descrição**: Cria um novo usuário e retorna um token JWT para autenticação.
- **Parâmetros de Requisição**:
  - **Body** (JSON):
    ```json
    {
      "name": "string",
      "email": "string",
      "password": "string"
    }
    ```
- **Resposta**:
  - **Status**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "jwt": "token_jwt_gerado"
    }
    ```
- **Códigos de Erro**:
  - `409 Conflict`: Email já registrado.

### **Login**

- **URL**: `/login`
- **Método**: `POST`
- **Descrição**: Autentica o usuário e retorna um token JWT para acesso aos endpoints protegidos.
- **Parâmetros de Requisição**:
  - **Body** (JSON):
    ```json
    {
      "email": "string",
      "password": "string"
    }
    ```
- **Resposta**:
  - **Status**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "jwt": "token_jwt_gerado"
    }
    ```
- **Códigos de Erro**:
  - `401 Unauthorized`: Credenciais inválidas.

### **Consultar Fato Aleatório (Protegido)**

- **URL**: `/consultar`
- **Método**: `GET`
- **Descrição**: Retorna um fato aleatório, acessível apenas para usuários autenticados via JWT.
- **Cabeçalho de Autenticação**:
  - `Authorization`: `Bearer {token_jwt}`
- **Resposta**:
  - **Status**: 200 OK
  - **Body**: Resposta da API de fatos aleatórios (o conteúdo pode variar).
- **Códigos de Erro**:
  - `403 Forbidden`: JWT ausente ou inválido.

## Autenticação

Para acessar o endpoint `/consultar`, o usuário precisa de um token JWT, que pode ser obtido no endpoint `/login`. O token deve ser enviado no cabeçalho de autenticação da requisição com o formato:

Authorization: Bearer {token_jwt}

--- 
## Configuração

### Rodar a API pelo terminal
Para configurar e rodar a API, instale as dependências e execute o servidor:

```bash
# Rode o docker compose dentro da raiz do projeto
docker compose up
 
``` 

Para testar a API, rode os scripts em python em ordem:
- ``testar_registro.py`` para criar um novo usuário
- ``testar_api.py `` para testar o login e a consulta do fato aleatório

Ou:
- Direto pelo terminal do seu sistema operacional com os comandos de request de acordo com cada endpoint que deseja testar (consultar tópico de endpoints)

---
# Screenshots da API e Vídeo Demonstrativo (PARTE 1)
--- 
## /registrar
Teste de registro de novo usuário:
![Teste registro - cadastro](./assets/test-register-1.png)  

Teste de tentativa de cadastro de usuário já existente:
![Teste registro - cadastro duplicado](./assets/test-register-2.png)  

## /login e /consultar
Teste de login e consulta de fato aleatório:
![Teste login e consulta](./assets/test-login-consultar.png)  

## Terminal do Docker
![Terminal Docker](./assets/test-terminal-1.png)
![Terminal Docker](./assets/test-terminal-2.png)


## Vídeo:
![Vídeo da API Rodando](./assets/Reunião com Beatriz Borges Zackiewicz-20241031_144919-Gravação de Reunião.mp4)

---
# Deploy na AWS (PARTE 2)
--- 
## Publicação na AWS

Para este projeto, os seguintes serviços AWS estão sendo utilizados:

- EKS (Elastic Kubernetes Service): Gerencia o cluster Kubernetes para implantar e orquestrar os contêineres.

- LoadBalancer: Criado automaticamente pelo Kubernetes no serviço EKS para expor a aplicação FastAPI ao público, permitindo acesso externo.

- EC2 (Elastic Compute Cloud): Fornece as instâncias de máquinas virtuais que hospedam os nós de trabalho do cluster Kubernetes.

- Amazon VPC: Proporciona uma rede isolada para os recursos do cluster, garantindo segurança e controle do tráfego de rede.

- IAM (Identity and Access Management): Configura permissões e roles para o Kubernetes interagir com outros serviços da AWS.

Esses serviços, juntos, criam a infraestrutura necessária para rodar uma aplicação em contêiner com alta disponibilidade e escalabilidade.

## Arquivos de Configuração de Kubernetes

A seguir estão os arquivos de configuração usados no Kubernetes e suas funções:

1. ``deployment.yml``:

- Este arquivo define o Deployment para a aplicação FastAPI.
- Configura o número de réplicas (neste caso, 1) e especifica a imagem do Docker a ser usada: beatrizbzack/projeto-cloud-app:latest.
- Configura variáveis de ambiente, como DATABASE_URL e SECRET_KEY, necessárias para a aplicação.
- Exemplo: Garante que a API FastAPI esteja disponível no cluster Kubernetes.


2. ``postgres-deployment.yml``:
- Define o Deployment para o banco de dados PostgreSQL.
- Configura as variáveis de ambiente como POSTGRES_DB, POSTGRES_USER e POSTGRES_PASSWORD.
- Inclui um volume para persistência dos dados, configurado para ser temporário (emptyDir).
- Exemplo: Proporciona o backend de banco de dados para a aplicação FastAPI.


3. ``service.yml``:

- Define os Services para a API FastAPI e o banco de dados PostgreSQL.
- Para a API:
  - Expõe o serviço como um LoadBalancer, permitindo acesso externo ao FastAPI na porta 80.
- Para o PostgreSQL:
  - Configura um serviço interno acessível na porta 5432 para os pods conectarem-se ao banco.
- Exemplo: Garante comunicação entre os componentes internos do cluster e expõe a API ao público. 

## Vídeo Demonstração AWS

Vídeo demonstrando o funcionamento da API

