from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.logger import log

class SQLAlchemy:
    def __init__(self, app:FastAPI = None, **kwargs):
        self._engine = None
        self._session = None

        if app is not None:
            self.initialize(app=app, **kwargs)

    
    def initialize(self, app:FastAPI, **kwargs):
        ''' DB 초기화 '''

        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)
        
        self._engine = create_engine(
            database_url,
            echo=echo,
            pool_recycle=pool_recycle,
            pool_pre_ping=True,
        )
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

        @app.on_event("startup")
        def startup():
            self._engine.connect()
            log.print("connected DB!")

        @app.on_event("shutdonw")
        def shutdonw():
            self._session.close_all()
            self._engine.dispose()
            log.print("disconnected DB!")


