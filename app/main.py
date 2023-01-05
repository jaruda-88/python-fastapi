import uvicorn
from dataclasses import asdict
from fastapi import FastAPI
from common.config import conf
from routers import index


def create_app():
    ''' 앱 함수 실행 '''

    app = FastAPI()

    # 라우터 정의
    app.include_router(index.router)

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)