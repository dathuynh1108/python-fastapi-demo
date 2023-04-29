from fastapi.encoders import jsonable_encoder
from fastapi import Response
from internal.demo.interface.http.entity.common import response
class controller(object):
    def __init__(self): pass

    def success( self, code: int, message: str, data: object):
        return response(code, message, data)
    
    def failure(self, code: int, message: str, data: object):
        return response(code, message, data)