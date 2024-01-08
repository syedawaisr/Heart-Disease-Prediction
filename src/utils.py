import os 
import sys
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error
from src.logger import logging
from src.exception import CustomException
import pickle


def save_object(file_path, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directory if it doesn't exist
        logging.info("Directory is created")

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Object saved successfully")
    except Exception as e:
        logging.error("Error while saving the object")
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.error("Error while loading the file")
        raise CustomException(e, sys)

