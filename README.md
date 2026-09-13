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
