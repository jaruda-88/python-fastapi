from datetime import datetime
from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()


@router.get("/")
async def index():
    '''
    상태 체크용 api
    :return: 
    '''
    currentTime = datetime.utcnow()
    return Response(f"API (UTC: {currentTime.strftime('%Y-%m-%d %H:%M:%S')})")