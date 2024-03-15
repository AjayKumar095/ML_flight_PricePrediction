import os
import logging
import pandas as pd 
import pickle as pkl 
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

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


class model_trainer:
    
    def __init__(self, train_data_file):
        self.train_data_file = train_data_file
        
    
    def model_training(self):
        
        try :
            
            logging.info('model training start.')
            
            train_data=pd.read_csv(self.train_data_file)
            
            ## seprating dependant and Independent featres.
            logging.info('seprating features')
            X=train_data.iloc[:, train_data.columns != 'Price']
            Y=train_data['Price']
            
            ## Spliting data into train and test part
            logging.info("Performing train test split")
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
            
            
            ## creating model
            logging.info('Creating model')
            regrasor=RandomForestRegressor()
            regrasor.fit(x_train, y_train)
            logging.info("Model created")
            
            ## Checking the model performance
            y_pred=regrasor.predict(x_test)
            
            Accuracy=r2_score(y_pred=y_pred, y_true=y_test)
            logging.info(f"Model accuracy: {Accuracy}")
            
            logging.info('creating pickle file of the model.')
            
            model_file_path='artifacts/model.pkl'
            with open(model_file_path, 'wb') as file:
               # dump information to that file
                pkl.dump(regrasor, file)
            return model_file_path    
            
        except Exception as e:
            logging.info("Model training failed.")        

