from fastapi import APIRouter

router = APIRouter(prefix='/content', tags=['content'])


@router.get('')
async def get_content():
    return


@router.post('/create')
async def create_content():
    return


@router.get('/{content_id}')
async def get_content_by_id(content_id: str):
    return


@router.delete('/{content_id}')
async def delete_content_by_id(content_id: str):
    return


@router.put('/{content_id}')
async def update_content_by_id(content_id: str):
    return
