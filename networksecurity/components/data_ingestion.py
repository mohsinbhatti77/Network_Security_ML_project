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
    
        