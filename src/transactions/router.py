from fastapi import APIRouter, Depends

from src.transactions.dao import TransactionsDAO
from src.transactions.schemas import STransaction
from src.users.dependencies import get_current_user
from src.users.models import Users

router = APIRouter(
    prefix='/transactions',
    tags=['Transactions'],
)


@router.get('')
async def get_transactions(user: Users = Depends(get_current_user)) -> list[
    STransaction]:
    return await TransactionsDAO.find_all(user_id=user.id)


@router.post('/add')
async def add_transaction(user: Users = Depends(get_current_user)):
    return await TransactionsDAO.add()
