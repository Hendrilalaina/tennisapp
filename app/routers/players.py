from fastapi import APIRouter

router = APIRouter(
    prefix='/players',
    tags=['Players'])

@router.get('/')
async def list_players():
    return []