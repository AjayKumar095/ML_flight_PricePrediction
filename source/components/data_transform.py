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

class Data_Transform:
    
    def __init__(self, file_path):
        
        self.file_path=file_path
        
    def data_transforming(self):
        
        try:
        
            logging.info("data transforming start")
            
            file_path_clean='artifacts/Train_data.csv'
            
            df=pd.read_csv(self.file_path)
            
            logging.info('File read into data frame.') 
            
            ## dropin null values
            df.dropna(inplace=True)
            
            df['day_of_journey']=pd.to_datetime(df['Date_of_Journey'], format="%d/%m/%Y" ).dt.day   ## making day_of_journey column
            df['month_of_journey']=pd.to_datetime(df['Date_of_Journey'], format="%d/%m/%Y" ).dt.month ## making month_of_journey column
            df.drop(['Date_of_Journey'], axis=1, inplace=True)
           
           # Departure time is when a plane leaves the gate. 
           # Similar to Date_of_Journey we can extract values from Dep_Time

            # Extracting Hours
            df["Dep_hour"] = pd.to_datetime(df["Dep_Time"], format='%H:%M').dt.hour

            # Extracting Minutes
            df["Dep_min"] = pd.to_datetime(df["Dep_Time"], format='%H:%M').dt.minute

            # Now we can drop Dep_Time as it is of no use
            df.drop(["Dep_Time"], axis = 1, inplace = True)
            
            # Arrival time is when the plane pulls up to the gate.
            # Similar to Date_of_Journey we can extract values from Arrival_Time

            # Extracting Hours
            df["Arrival_hour"] = pd.to_datetime(df['Arrival_Time']).dt.hour

            # Extracting Minutes
            df["Arrival_min"] = pd.to_datetime(df['Arrival_Time']).dt.minute

            # Now we can drop Arrival_Time as it is of no use
            df.drop(["Arrival_Time"], axis = 1, inplace = True)
                       
            ## we have a feature name duration since there is no direct connection with the target feature. Duration is the difference of date of jounrey and arrival time.
            ## it cannot take as a input from user, so we can drop it

            df.drop('Duration', axis=1, inplace=True)      
            
            ## similarly Route and total_stop both are related to each other,
            ## And 80% of Additional_Info have no info,
            ## So we drop both the column route and Additional_Info.

            df.drop(['Additional_Info', 'Route'], axis=1, inplace=True)   
            
          
            
            
            
            ## Applying OneHotEncodeing on Aireline

            Airline = df[["Airline"]]

            airline = pd.get_dummies(Airline, drop_first= True)
            
            ## Applying OneHotEncodeing on Source

            Source = df[["Source"]]

            source = pd.get_dummies(Source, drop_first= True)
            
            ## Applying OneHotEncodeing on Destination

            Destination = df[["Destination"]]

            destination = pd.get_dummies(Destination, drop_first= True)
            
            # As this is case of Ordinal Categorical type we perform LabelEncoder
            # Here Values are assigned with corresponding keys

            df.replace({"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}, inplace = True)
            
            # Concatenate dataframe --> train_data + Airline + Source + Destination

            df = pd.concat([df, airline, source, destination], axis = 1)
            
            ## Now we have to drop Airline, Source, Destination

            df.drop(['Airline', 'Source', 'Destination'], axis=1, inplace=True)
                        
            ## saving the finall dataframe in csv file

            df.to_csv(file_path_clean, index=None)
            
            logging.info('Data Transformation Complete.') 
            
            return file_path_clean
        
        except Exception as e:
            logging.info(f'Data Transformation Failed. {e}')   



