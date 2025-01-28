from fastapi import APIRouter

router = APIRouter(prefix='/payments', tags=['payments'])


@router.post('/create')
async def create_payments():
    return


@router.get('/transactions')
async def get_transactions():
    return


@router.get('/transactions/{transaction_id}')
async def get_transaction(transaction_id: str):
    return
