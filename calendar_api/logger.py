import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, "fastapi_app.log")

    # Configure logger
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[
                            logging.StreamHandler(),
                            RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=5)
                        ])
