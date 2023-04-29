import logging
from internal.demo.interface.http import http
from internal.demo.service import health_service

class handler(object):
    def __init__(self) -> None:
        self.health_service = health_service.health_service()
        self.http_interface = http.http_interface(self.health_service)
        self.logger = logging.getLogger(__name__)
        self.logger.info("initializing handler")
    
    def start(self):
        self.logger.info("starting handler")
        self.http_interface.start()
        

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename='demo.log', 
    encoding='utf-8',
)

LOG_LEVEL: str = "DEBUG"
FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging_config = {
    "version": 1, # mandatory field
    # if you want to overwrite existing loggers' configs
    # "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": FORMAT,
        }
    },
    "handlers": {
        "console": {
            "formatter": "basic",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "level": LOG_LEVEL,
        }
    },
    "loggers": {},
}
