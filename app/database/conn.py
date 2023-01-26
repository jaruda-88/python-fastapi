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
        ''' 
        DB 초기화
        :param app: FastAPI instance
        :param kwargs:
        :return:
        '''

        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)
        
        self._engine = create_engine(
            database_url,
            echo=echo,  # log
            pool_recycle=pool_recycle, # mysql 경우 일정 시간 이후 강제로 끊어지는데 n초 이후로 connection을 재사용
            pool_pre_ping=True, # db 접속전에 간단한 쿼리문을 ping처럼 날려 connection 을 확인하고, 연결
        )
        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

        @app.on_event("startup")
        def startup():
            self._engine.connect()
            log.debug("connected DB!")

        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()
            log.debug("disconnected DB!")

    
    def get_db(self):
        ''' 
        db 세션 유지 함수 
        :return:
        '''

        if self._session in None:
            raise Exception("called initialize")

        db_session = None

        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    
    @property
    def session(self):
        return self.get_db

    
    @property
    def engine(self):
        return self._engine
        

db = SQLAlchemy()
Base = declarative_base()