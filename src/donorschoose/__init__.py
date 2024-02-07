import os
import sys
import logging

"""
logging template
time:leveloflog:modulename(dir name where error occure):message
"""
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#create logging dir to save loggers 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        #saving logs in running logs
        logging.FileHandler(log_filepath),
        #print logger in terminal
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("donorschooseLogger")