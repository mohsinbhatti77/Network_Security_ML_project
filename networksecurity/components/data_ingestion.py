from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entiy import DataIngestionConfig
import os 
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import List 
import pymongo
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    
        
        
    """ Read The Data """
    def export_data_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df.drop(columns=["_id"])  
            df.replace({"na":np.nan}, inplace=True)  
            return df  
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
        
    def export_data_into_feature_store(self, dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # FOR CREATING FOLDER
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
   
   
   
        
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_data_as_dataframe()
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
        
    
            