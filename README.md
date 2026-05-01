# oracle-ai-template

Base template for all oracle-ai-* repos in this portfolio.
Use this template to initialize any new Oracle AI repo in 30 seconds.

---

## How to Use This Template

1. Click **Use this template** → **Create a new repository**
2. Name your repo (e.g. `oracle-ai-hello`)
3. Clone it and run:

```bash
git clone https://github.com/YOURUSERNAME/your-new-repo.git
cd your-new-repo
cp .env.example .env        # fill in your credentials
pip install -r requirements.txt
pre-commit install
python generate_fixtures.py
python main.py
```

---

## What's Included

| File | Purpose |
|------|---------|
| `.env.example` | All required environment variables |
| `.gitignore` | Keeps credentials and outputs off GitHub |
| `requirements.txt` | All Python dependencies |
| `generate_fixtures.py` | Creates synthetic Oracle data |
| `src/db_connect.py` | Reusable Oracle connection helper |
| `DATA.md` | Synthetic data documentation |
| `ARCHITECTURE.md` | System diagram + design decisions |
| `tests/test_placeholder.py` | Passing tests from day one |
| `.github/workflows/ci.yml` | GitHub Actions CI |
| `.pre-commit-config.yaml` | Auto-formatting on every commit |
| `Dockerfile` | Container packaging for client delivery |

---

## Fictional Company
All repos use **GlobalManufacturing Corp** synthetic data.
- CORP_US — United States
- CORP_EMEA — Europe, Middle East, Africa
- CORP_APAC — Asia Pacific

---

## Tech Stack
- Oracle Autonomous Database 23ai (Always Free)
- python-oracledb 2.x — wallet-based mTLS connection
- LiteLLM — provider-agnostic LLM routing
- LangSmith — agent tracing
- AgentOps — agent lifecycle monitoring
- Langfuse — prompt version management
- pytest + GitHub Actions CI
- Docker

---

## Portfolio Repos Built From This Template

| Repo | Description |
|------|-------------|
| oracle-ai-hello | Python + Oracle + Azure OpenAI AP aging report |
| oracle-erp-rag | RAG over Oracle finance documents |
| oracle-mcp-server | Oracle Fusion REST as MCP tools |
| oracle-ap-invoice-agent | LangGraph AP invoice hold resolution |
| oracle-idp-ap-automation | Azure Document Intelligence + Oracle AP |
| oracle-ai-finance-copilot | crewAI + LangGraph finance copilot |
| oracle-month-end-close-agent | 23-step period close automation |
| oracle-audit-compliance-agent | SOD/SOX compliance detection |
| oracle-supplier-risk-agent | Supplier risk scoring with RAG |
| oracle-mes-ai | MPDV MES + Oracle AI agents |
| oracle-forecasting-agent | ASCP + Demantra AI analysis |
| oracle-ai-tools | pip install oracle-ai-tools |
| oracle-workflow-automation | n8n + OIC + BPM REST workflows |
