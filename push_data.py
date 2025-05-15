import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd 
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
        
def csv_to_json_converter(self, file_path):
    try:
        data = pd.read_csv(file_path)
        data.reset_index(drop=True, inplace=True)
        records =json.load(data.T.to_json()).values()
        return records
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
# 12 mint
        
        