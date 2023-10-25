import logging
from datetime import datetime

class Logger:
    def log(self,file_name,request_str):
        logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} - {request_str}"
        logging.info(log_message)