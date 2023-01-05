from dataclasses import dataclass, asdict
from os import path, environ
from pickle import TRUE

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    ''' 기본 configuration '''

    BASE_DIR = base_dir

    DEBUG: bool = False
    PROJ_RELOAD: bool = False


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


@dataclass
class LocalConfig(Config):
     PROJ_RELOAD: bool = False


@dataclass
class TestConfig(Config):
    DEBUG: bool = True
    PROJ_RELOAD: bool = True


def conf():
    ''' 
    환경 불려오기
    :return:
    '''
    config = dict(prod=ProdConfig(), local=LocalConfig(), test=TestConfig())
    # dict = asdict(TestConfig())
    return config.get(environ.get("API_ENV", "test"))