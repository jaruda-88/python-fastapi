from dataclasses import dataclass, asdict
from os import path, environ
from pickle import TRUE

base_dir = path.dirname(path.dirname(path.abspath(__file__)))


@dataclass
class Config:
    ''' 기본 configuration '''

    BASE_DIR = base_dir

    DEBUG: bool = False
    DB_URL: str = environ.get("DB_URL", "")
    DB_ECHO: bool = True
    DB_POOL_RECYCLE: int = 900


@dataclass
class ProdConfig(Config):
    DEBUG: bool = False


@dataclass
class LocalConfig(Config):
    DEBUG: bool = True


@dataclass
class TestConfig(Config):
    DEBUG: bool = True
    DB_URL: str = "mysql+pymysql://admin:amdin@localhost/tb_base?charset=utf8mb4"


def conf():
    ''' 
    환경 불려오기
    :return:
    '''
    config = dict(prod=ProdConfig(), local=LocalConfig(), test=TestConfig())
    # dict = asdict(TestConfig())
    return config.get(environ.get("API_ENV", "test"))