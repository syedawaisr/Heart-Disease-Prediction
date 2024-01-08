import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import data_transform
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from src.utils import save_object
#from src.utils import evaluate_model
from dataclasses import dataclass


@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifact','model1.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_training(self,x_train, x_test, y_train, y_test):
        # SVC Classifier
        svc_classifier = SVC(kernel='linear', random_state=42)
        svc_classifier.fit(x_train, y_train)
        y_pred_svc = svc_classifier.predict(x_test)
        accuracy_svc = accuracy_score(y_test, y_pred_svc)
        print(f"Accuracy of SVC: {accuracy_svc}")

        # Random Forest Classifier
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_classifier.fit(x_train, y_train)
        y_pred_rf = rf_classifier.predict(x_test)
        accuracy_rf = accuracy_score(y_test, y_pred_rf)
        print(f"Accuracy of Random Forest: {accuracy_rf}")

        # KNN Classifier
        knn_classifier = KNeighborsClassifier(n_neighbors=5)
        knn_classifier.fit(x_train, y_train)
        y_pred_knn = knn_classifier.predict(x_test)
        accuracy_knn = accuracy_score(y_test, y_pred_knn)
        print(f"Accuracy of KNN: {accuracy_knn}")

        best_model = svc_classifier


        save_object(
            file_path=self.model_trainer_config.trained_model_file_path,
            obj=best_model
            
            )
 
# if __name__ == "__main__":
#     data = DataIngestion()
#     df = data.initiate_data_ingestion()
#     tr = data_transform()
#     x_train, x_test, y_train, y_test = tr.initiate_data_transform(df)
#     print(x_train)
#     train = ModelTrainer()

#     train.initiate_training(x_train, x_test, y_train, y_test)