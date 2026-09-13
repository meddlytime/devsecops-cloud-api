<div align="center">

# 🛡️ DevSecOps Cloud API

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Alpine_Hardened-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)
[![Security](https://img.shields.io/badge/Vulnerabilities-0_Critical-brightgreen?style=for-the-badge&logo=docker)](https://scout.docker.com)

**API RESTful assíncrona focada em hardening de contêineres, arquitetura resiliente e boas práticas de DevSecOps.**

[ 🇧🇷 Português ](#-português) • [ 🇺🇸 English ](#-english)

</div>

---

## 🇧🇷 Português

### 📌 Visão Geral do Projeto
Esta aplicação é uma API RESTful de alta performance projetada sob os conceitos modernos de **DevSecOps** e **Cloud Native**. O objetivo central é demonstrar a construção de microsserviços seguros, desde a escrita de código assíncrono com **FastAPI** até o fortalecimento (*hardening*) da imagem Docker para mitigação de vulnerabilidades conhecidas (CVEs) e isolamento de privilégios.

---

### 🚀 Arquitetura & Tecnologias

| Componente | Tecnologia | Função / Aplicação |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.12 | Desenvolvimento do backend assíncrono |
| **Framework** | FastAPI | Roteamento, documentação automática (Swagger/OpenAPI) e validação Pydantic |
| **Servidor ASGI** | Uvicorn | Processamento assíncrono de requisições de alta concorrência |
| **Contêiner** | Docker (Alpine 3.12) | Isolamento leve da aplicação e empacotamento para nuvem |
| **Auditoria** | Docker Scout | Análise contínua de vulnerabilidades de segurança (SCA) |
| **Testes** | Pytest / TestClient | Testes de integração e asserção automática de endpoints |

---

### 🔒 Práticas de Segurança & Hardening (DevSecOps)

- **Redução de Superfície de Ataque:** Substituição da imagem padrão pela base minimalista `python:3.12-alpine`. O número total de pacotes de sistema instalados foi reduzido de 365 para 25, eliminando superfícies de exploração desnecessárias.
- **Princípio do Menor Privilégio (*Non-Root Enforcement*):** Criação e alternância explícita para o usuário `appuser`. O contêiner não é executado com privilégios de `root`, impedindo a movimentação lateral ou elevação de privilégios no nó hospedeiro (*host*) em casos de execução remota de código (RCE).
- **Monitoramento de Saúde (*Healthchecks*):** Instrução `HEALTHCHECK` configurada nativamente dentro do `Dockerfile` para verificação periódica de integridade da API via endpoint `/health`, permitindo auto-recuperação em orquestradores como AWS ECS e Kubernetes.
- **Gestão de Cache e Permissões:** Limpeza de instalações temporárias via `--no-cache-dir` no `pip` e ajuste restrito de propriedade de pastas com `chown -R appuser:appuser /app`.

#### 📊 Métricas de Auditoria (Docker Scout)

| Métrica | Antes (python:3.12-slim) | Depois (python:3.12-alpine) | Impacto de Segurança |
| :--- | :--- | :--- | :--- |
| **Vulnerabilidades Críticas (CVEs)** | 5 Critical | **0 Critical** | Erradicação total de riscos de alto impacto |
| **Privilégio do Usuário** | `root` (UID 0) | `appuser` (UID não-root) | Prevenção contra estouro de contêiner |
| **Total de Pacotes do SO** | 365 pacotes | **25 pacotes** | Redução de 93% na superfície de código vulnerável |

---

### 📂 Estrutura do Repositório

```text
.
├── .dockerignore      # Arquivos excluídos do contexto de build do Docker
├── .gitignore         # Filtro preventivo de arquivos temporários e ambientes virtuais
├── Dockerfile         # Receita endurecida e otimizada da imagem Docker
├── main.py            # Regras de negócio da API FastAPI e endpoints
├── requirements.txt   # Dependências diretas do projeto em Python
├── test_main.py       # Suíte de testes automatizados com Pytest
└── README.md          # Documentação técnica bilíngue do repositório
```

---

### 🌐 Referência de Endpoints (API)

| Método | Rota | Descrição | Status HTTP Esperado |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Retorna mensagem de boas-vindas e status da API | `200 OK` |
| `GET` | `/health` | Checagem de integridade para monitoramento e Load Balancers | `200 OK` |
| `POST` | `/items/` | Processa e valida cargas de dados enviadas via payload JSON | `201 Created` / `422 Unprocessable` |

---

### 🛠️ Instalação, Execução e Testes

#### 1. Construção e Execução do Contêiner
```bash
# Construir a imagem otimizada localmente
docker build -t devsecops-cloud-api .

# Executar o contêiner mapeando a porta 8000
docker run -d -p 8000:8000 --name api-container devsecops-cloud-api
```

#### 2. Execução Local dos Testes (Pytest)
```bash
# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou no Windows: venv\Scripts\activate

# Instalar dependências e rodar os testes
pip install -r requirements.txt
pytest
```

*Acesse a interface interativa do Swagger UI em: `http://localhost:8000/docs`*

---

## 🇺🇸 English

### 📌 Project Overview
This application is a high-performance RESTful API built on modern **DevSecOps** and **Cloud Native** principles. Its primary objective is to demonstrate secure microservices architecture, spanning from asynchronous Python development with **FastAPI** to container **hardening** via Docker, mitigating known common vulnerabilities and exposures (CVEs) and enforcing strict privilege separation.

---

### 🚀 Architecture & Tech Stack

| Component | Technology | Primary Role / Context |
| :--- | :--- | :--- |
| **Language** | Python 3.12 | Asynchronous backend implementation |
| **Framework** | FastAPI | Routing, interactive documentation (OpenAPI/Swagger), and Pydantic validation |
| **ASGI Server** | Uvicorn | Asynchronous request processing for high-concurrency workloads |
| **Containerization** | Docker (Alpine 3.12) | Lightweight runtime isolation and cloud packaging |
| **Audit & Security** | Docker Scout | Continuous Software Composition Analysis (SCA) |
| **Automated Testing** | Pytest / TestClient | Integration testing and automated endpoint validation |

---

### 🔒 Security Practices & Hardening (DevSecOps)

- **Attack Surface Reduction:** Replaced heavy standard base images with `python:3.12-alpine`. Total installed OS packages were reduced drastically from 365 to 25, eliminating unneeded binaries and system libraries.
- **Least Privilege Principle (Non-Root Enforcement):** Configured and enforced execution under a dedicated non-root `appuser`. The container avoids running as `root`, preventing privilege escalation onto the host machine in the event of Remote Code Execution (RCE).
- **Native Container Health Checking:** Integrated `HEALTHCHECK` directive directly into the `Dockerfile` to enable periodic API status checks via `/health`, allowing automatic recovery on orchestrators like AWS ECS or Kubernetes.
- **Clean Image Footprint:** Suppressed cache creation using `pip`'s `--no-cache-dir` flag and explicitly restricted file ownership with `chown -R appuser:appuser /app`.

#### 📊 Security Audit Metrics (Docker Scout)

| Metric | Baseline (python:3.12-slim) | Hardened (python:3.12-alpine) | Security Impact |
| :--- | :--- | :--- | :--- |
| **Critical Vulnerabilities (CVEs)** | 5 Critical | **0 Critical** | Complete mitigation of high-severity risks |
| **User Privilege** | `root` (UID 0) | `appuser` (Non-root UID) | Host breakout prevention |
| **OS Packages Installed** | 365 packages | **25 packages** | 93% reduction in attack surface |

---

### 📂 Repository Structure

```text
.
├── .dockerignore      # Excluded files from Docker build context
├── .gitignore         # Preventive filter for virtualenvs and temporary files
├── Dockerfile         # Hardened container specification
├── main.py            # FastAPI core logic and application endpoints
├── requirements.txt   # Python project dependencies
├── test_main.py       # Automated integration test suite using Pytest
└── README.md          # Bilingual technical documentation
```

---

### 🌐 API Endpoint Reference

| Method | Route | Description | Expected HTTP Status |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Welcoming message and basic runtime status | `200 OK` |
| `GET` | `/health` | Health check probe for orchestrators and Load Balancers | `200 OK` |
| `POST` | `/items/` | Receives, validates, and processes JSON payloads | `201 Created` / `422 Unprocessable` |

---

### 🛠️ Setup, Execution & Testing

#### 1. Container Build and Deployment
```bash
# Build hardened image locally
docker build -t devsecops-cloud-api .

# Run container mapping port 8000
docker run -d -p 8000:8000 --name api-container devsecops-cloud-api
```

#### 2. Local Test Execution
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or Windows: venv\Scripts\activate

# Install dependencies and trigger Pytest
pip install -r requirements.txt
pytest
```

*Access interactive Swagger UI documentation at: `http://localhost:8000/docs`*
