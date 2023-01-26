from dataclasses import dataclass, asdict
from os import path, environ
from pickle import TRUE

base_dir = path.dirname(path.dirname(path.abspath(__file__)))

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",

        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "debug-log": {"handlers": ["default"], "level": "DEBUG"},
    },
}

@dataclass
class Config:
    ''' 기본 configuration '''

    BASE_DIR = base_dir

    DEBUG: bool = False
    DB_HOST: str = ""
    DB_USER: str = environ.get("MYSQL_USER", "admin")
    DB_PWD: str = environ.get("MYSQL_PASSWORD", "admin")
    DB_PORT: int = 0
    DB_DATABASE: str = environ.get("MYSQL_DATABASE", "tb_base")
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
    DB_HOST: str = "192.168.0.100"
    DB_PORT: int = 3307
    DB_URL: str = f"mysql+pymysql://{Config.DB_USER}:{Config.DB_PWD}@{DB_HOST}:{DB_PORT}/{Config.DB_DATABASE}?charset=utf8mb4"


def conf():
    ''' 
    환경 불려오기
    :return:
    '''
    config = dict(prod=ProdConfig(), local=LocalConfig(), test=TestConfig())
    # dict = asdict(TestConfig())
    return config.get(environ.get("API_ENV", "test"))