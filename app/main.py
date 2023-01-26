import uvicorn
from dataclasses import asdict
from fastapi import FastAPI
from common.config import conf
from routers import index
from utils.logger import log
from database.conn import db
# import logging


def create_app():
    ''' 
    앱 실행 
    :return:
    '''

    app = FastAPI()

    config = conf()
    dictConfig = asdict(config)

    # logger 정의
    log.initialize(app, **dictConfig)

    # db 정의
    db.initialize(app, **dictConfig)

    # 라우터 정의
    app.include_router(index.router)

    log.print("created app!")
    
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)