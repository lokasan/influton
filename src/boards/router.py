from fastapi import APIRouter
from src.boards.schemas import BoardContent

router = APIRouter(prefix='/boards', tags=['boards'])


@router.get('')
async def get_boards():
    return


@router.post('/create')
async def create_board():
    return


@router.get('/{board_id}')
async def get_board(board_id: str):
    return


@router.get('/{board_id}/content')
async def get_board_content(board_id: str):
    return


@router.put('/{board_id}/content')
async def update_board_content(board: BoardContent):
    return {'board_id': board.id}

