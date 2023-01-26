import logging

class Logger():
    def __init__(self, name:str = '', **kwargs):
        self._logger = None
        self._mode : bool = False

        if name != '':
            self.initialize(name, **kwargs)


    def initialize(self, name:str, **kwargs):
        '''
        loggger 초기화
        :param app: FastAPI instance
        :param kwargs:
        :return:
        '''
        
        self._logger = logging.getLogger(name)
        self._mode = kwargs.setdefault("DEBUG", False)
    

    def debug(self, *args):
        '''
        debug log
        :param args: content
        :return:
        '''

        if self._mode == True:
            self._logger.debug(args)


    def print(self, *args):
        '''
        info log
        :param args: content
        :return:
        '''

        self._logger.info(args)

log = Logger()

