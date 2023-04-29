import logging
import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from internal.demo.interface.http.controller import health_controller
from internal.demo.interface.http.entity.common import response
from internal.demo.service import health_service

class http_interface(object):
    def __init__(
        self, 
        health_service: health_service.health_service
    ) -> None:        
        self.health_controller = health_controller.health_controller(health_service)
        
        self.app = fastapi.FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["DELETE", "GET", "POST", "PUT"],
            allow_headers=["*"],
        )
        self.init_route()
    
    def init_route(self):
        router = fastapi.routing.APIRouter()
        router.add_api_route(
            "/api/health", 
            endpoint=self.health_controller.get_health, 
            methods=["GET"],
        )
        self.app.include_router(router)

    def start(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8080)


        