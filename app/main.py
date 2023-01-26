import uvicorn
from dataclasses import asdict
from fastapi import FastAPI
from common.config import conf, log_config
from routers import index
from utils.logger import log
from database.conn import db
from logging.config import dictConfig

def create_app():
    ''' 
    앱 실행 
    :return:
    '''

    config = conf()
    dictConf = asdict(config)

    app = FastAPI(debug=dictConf.get("DEBUG"))

    # logger 정의
    dictConfig(log_config)
    log.initialize('debug-log', **dictConf)

    # db 정의
    db.initialize(app, **dictConf)

    # 라우터 정의
    app.include_router(index.router)

    log.debug("created app!")
    
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)