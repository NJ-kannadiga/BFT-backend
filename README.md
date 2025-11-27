# Finance Tracker - Backend (FastAPI)

This is a scaffolded FastAPI backend for your Finance Tracker frontend.

### Quick start (with Docker)
1. Copy `.env.template` to `.env` and set `SECRET_KEY`.
2. Build and run:
```bash
docker-compose up --build
```
3. Backend will be available at `http://localhost:8000` and OpenAPI at `http://localhost:8000/docs`.

### Endpoints (summary)
- `POST /api/auth/register` — register (body: username, email, password)
- `POST /api/auth/token` — login (form data: username, password) returns bearer token
- `GET /api/accounts` — list accounts (auth required)
- `POST /api/accounts` — create account
- `GET /api/categories` — list categories
- `POST /api/categories` — create category
- `GET /api/transactions` — list transactions
- `POST /api/transactions` — create transaction
- `GET /api/reports/monthly` — monthly summary

### Notes
- This scaffold uses synchronous SQLAlchemy for simplicity. If you'd prefer async SQLAlchemy or SQLModel, tell me and I can convert.
- I matched common endpoint shapes to your frontend. If you want exact paths/payloads inferred from your React code, I can map them next.
