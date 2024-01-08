import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


from src.components.data_ingestion import DataIngestion


@dataclass
class data_transform_config:
    preprocessing_path = os.path.join("artifact","prerocessing.pkl")


class data_transform:
    def __init__(self):
        self.transformConfig = data_transform_config()

    def initiate_data_transform(self,df1): # train and test paths will be get by calling data_ingestion 
        #initiate_data_ingestion function which returns train and test path which will be passed here then 

 
        '''
        take the train and test.csv files, separate target column and features and apply all the preprocssing that is applied in jupyter notebook using transformers 
        before transformer better apply self made techniques like yes no mapping to 0 and 1 and datetime converstion in separate columns
        then separete all num and categorical columns and send them to respective num and cat pipelines where all one hot encoding
        and standard scalling will be applied, all this transformation and conversion part is done in preprocessing function
        
        1. In this function, take train and test data and then call Preprocessingdata().fit
        and transform to transform the data, this preprocessingdata is the above function which should be created according to dataset

        2. the above step will return values in arrays so you have to continate target by converting it into an array as 
        train_features  = preprocessing.fit_transform(train_feature_data)
        test_features =  preprocessing.transform(test_feature_data)
        train_preprocessed_data = np.to_c(train_features,np.array(train_target))
        '''

        try:
            df = df1
            # Converting all columns to int datatype
            for column in df.columns:
                if column!='Class':
                    df[column] = df[column].astype('int32')
            # call the preprocessor here
            class_mapping = {
            'Normal': 0,
            'Nromal':0,
            'Border Line': 1,
            'Borderline': 1,
            'High Risk': 2
            }

            #  Replace values in the 'Class' column based on the mapping
            df['Class'] = df['Class'].replace(class_mapping)
            x = df.iloc[:,1:]
            y = df["Class"]
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
            

            return(x_train, x_test, y_train, y_test)
        
        except Exception as e:
            logging.info("Error while fit and transform of preprocessing")
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    data = DataIngestion()
    df = data.initiate_data_ingestion()
    tr = data_transform()
    x_train, x_test, y_train, y_test = tr.initiate_data_transform(df)
        