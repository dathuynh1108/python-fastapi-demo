from fastapi.responses import JSONResponse
class response(JSONResponse):
    def __init__(self, code: str, message: int, data: object):
        content = {
            "code": code,
            "message": message,
            "data": data
        }
        super().__init__(content=content, status_code=code)