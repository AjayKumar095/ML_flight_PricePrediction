import pickle as pkl
from Logging import logs
from source.components.data_intake import Data_Intake
from source.components.data_transform import Data_Transform
from source.model.model_train import model_trainer


if __name__ == "__main__":
    
    logs.info("Data Intake Start")
    file_path=Data_Intake.add_raw_data()
    logs.info("Data Intake Complete.")
    
    logs.info('Data Transformation start')
    transform_data=Data_Transform(file_path)
    train_data_file_path=transform_data.data_transforming()
    logs.info("Data Transformation complete.")
    
    logs.info("Model Training Started")
    train_model=model_trainer(train_data_file_path)
    model_pkl_file=train_model.model_training()
    logs.info("Model trained")
    
  