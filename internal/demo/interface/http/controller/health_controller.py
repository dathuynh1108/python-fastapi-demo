from internal.demo.interface.http.controller import controller
from internal.demo.service import health_service
from internal.demo.service import health_service
from fastapi import Request, Response, status

import logging

class health_controller(controller.controller):
    def __init__(
        self, 
        health_service: health_service.health_service,
    ): 
        self.health_service = health_service
        self.logger = logging.getLogger(__name__)
    
    async def get_health(
        self,
        request: Request, 
        response: Response,
    ):
        self.logger.info(request)
        return self.success(
            status.HTTP_200_OK,
            self.health_service.get_health(),
            None, 
        )
        
