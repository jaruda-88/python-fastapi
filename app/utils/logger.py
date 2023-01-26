from fastapi import FastAPI
import logging

class Logger():
    def __init__(self, app:FastAPI=None, **kwargs):
        self._mode : bool = False

        if app is not None:
            self.initialize(app=app, **kwargs)


    def initialize(self, app:FastAPI, **kwargs):
        '''
        loggger 초기화
        :param app: FastAPI instance
        :param kwargs:
        :return:
        '''

        self._mode = kwargs.get("DEBUG")
    

    def print(self, *args):
        '''
        console log
        :param args: log context
        :return:
        '''

        if self._mode == True:
            logging.info(args)

log = Logger()

