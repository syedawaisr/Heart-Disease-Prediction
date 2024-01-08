import os
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class data_ingestion_config:
    # train_data_path = os.path.join("artifact","train.csv")
    # test_data_path  = os.path.join("artifact","test.csv")
    raw_data_path = os.path.join("artifact","Data of Patients with heart condition.xlsx")

class DataIngestion:
    def __init__(self):
        self.IngestionConfig = data_ingestion_config()
    def initiate_data_ingestion(self):
        logging.info("inititate data ingestion start")
        try:
            # write code here
            df=pd.read_excel(os.path.join("artifact","Data of Patients with heart condition.xlsx"), sheet_name='3-class')
            logging.info("Data read as pandas dataframe")
            os.makedirs(os.path.dirname(self.IngestionConfig.raw_data_path),exist_ok=True)
            #df.to_csv(self.IngestionConfig.raw_data_path,index=False)

            logging.info("raw data dir is made")
            print(df)

            return df


            # train_set,test_set = train_test_split(df,test_size=0.3, random_state=42)
            # logging.info("train_test_split")

            # train_set.to_csv(self.IngestionConfig.train_data_path,index = False, header = True)
            # test_set.to_csv(self.IngestionConfig.test_data_path, index=False, header = True)
            # logging.info("data ingestion is completed")

        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    data = DataIngestion()
    data.initiate_data_ingestion()