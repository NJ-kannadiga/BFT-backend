from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, transactions, categories, accounts, reports, goals

def create_app():
    app = FastAPI(title="Finance Tracker API")

    origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ]

    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=origins,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
    # app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
    # app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
    # app.include_router(accounts.router, prefix="/api/accounts", tags=["accounts"])
    # app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
    # app.include_router(goals.router, prefix="/api/goals", tags=["goals"])

    return app

app = create_app()
