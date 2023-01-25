from fastapi import FastAPI
import logging

class Logger():
    def __init__(self, app:FastAPI=None, **kwargs):
        self._mode : bool = False

        if app is not None:
            self.initialize(app=app, **kwargs)


    def initialize(self, app:FastAPI, **kwargs):
        self._mode = kwargs.get("DEBUG")
    

    def print(self, *args):

        if self._mode:
            logging.info(args)

log = Logger()

