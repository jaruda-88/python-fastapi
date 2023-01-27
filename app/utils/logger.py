import logging

class Logger():
    def __init__(self, name:str = '', debug:bool = False):
        self._logger = None
        self._mode : bool = debug

        if name != '':
            self.initialize(name, debug)


    def initialize(self, name:str, debug: bool):
        '''
        loggger 초기화
        :param app: FastAPI instance
        :param kwargs:
        :return:
        '''
        
        self._logger = logging.getLogger(name)
        self._mode = debug
    

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

