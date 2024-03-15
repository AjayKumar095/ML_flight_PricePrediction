import pandas as pd 
import logging
import os

# Create a folder for logs if it doesn't exist
log_folder = 'Source_Logs'
os.makedirs(log_folder, exist_ok=True)

# Specify the path to the log file within the folder
log_file_path = os.path.join(log_folder, 'source.log')

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format="[%(asctime)s: ] %(lineno)d  %(module)s: %(name)s: %(message)s:",  # Define the log format
    filename=log_file_path,  # Specify the log file path
      # Set file mode to 'write' to overwrite existing log file
)


class Data_Intake:
    
    def add_raw_data():
        try: 
            
            logging.info("addind raw data from Testing dir.")
            file_path='artifacts/raw_data.csv'
            df=pd.read_csv("Testing/data/Data_Train.csv")
            df.to_csv(file_path, index=None)
            
            
            logging.info("data added")
            return file_path
            
        except Exception as e:
            logging.info(f'data adding failed: {e}')

