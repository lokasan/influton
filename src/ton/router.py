from fastapi import APIRouter

router = APIRouter(prefix='/ton', tags=['ton'])


@router.get('/wallet')
async def get_wallet():
    pass


@router.get('/transactions')
async def get_transactions():
    pass
