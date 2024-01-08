import os
import sys
from src.logger import logging
from src.exception import CustomException

'''
This function is to get the value from user using any application and then predicring its value and also store it in the dataset
1. create web app to get the data from use (only allow compatible formate of input data)
2. store the data in dataset
3. pass the data to data_transform for preprocessing
4. call the evaluation function to get the best model
5. call the best model to predict the value

'''

import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd





class PredictPipeline:


    def predict(self,heart_rate, cholesterol_level, triglycerides_level, fasting_blood_sugar):
        try:
            # preprocessor_path=os.path.join('artifact','preprocessor.pkl')
            model_path=os.path.join('artifact','model1.pkl')

            # preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            # data_scaled=preprocessor.transform(features)

            
            custom_data_input_dict = {
            'Heart Rate':[heart_rate],
            'Cholestrol Level':[cholesterol_level],
            'Triglycerides Level':[triglycerides_level],
            'Fasting Blood Sugar':[fasting_blood_sugar]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("data frame of predicted data created")

            predict=model.predict(df)

            # Mapping numerical predictions to corresponding label strings
            prediction_mapping = {
                0: 'Normal',
                1: 'Border Line',
                2: 'High Risk'
            }
            # Mapping numeric predictions to label strings
            predicted_labels = [prediction_mapping[pred] for pred in predict]

            return predicted_labels[0]
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)

