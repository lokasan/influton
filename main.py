from fastapi import FastAPI

from src.boards.router import router as boards_router
from src.content.router import router as content_router
from src.payments.router import router as payments_router
from src.ton.router import router as ton_router
from src.users.router import router as users_router
from src.transactions.router import router as transactions_router

app = FastAPI()

app.include_router(boards_router)
app.include_router(content_router)
app.include_router(payments_router)
app.include_router(ton_router)
app.include_router(users_router)
app.include_router(transactions_router)
