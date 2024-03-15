import os
import sys
import logging



log_folder='Main_file_logs'   # creating log folder

log_file_name=os.path.join(log_folder, 'logging_info.log')  # creating log file inside the log folder

os.makedirs(log_folder, exist_ok=True)  # Checking the folder and saving it

log_info= "[%(asctime)s: ] %(lineno)d  %(module)s: %(name)s: %(message)s:"  # infoemation to store in log file


## Basic Config 

logging.basicConfig(
    level=logging.INFO,
    format=log_info,
    
    handlers=[
        logging.FileHandler(log_file_name),
        logging.StreamHandler(sys.stdout)
    ]
)

logs=logging.getLogger("Custom logging.")

