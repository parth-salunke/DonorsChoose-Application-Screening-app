import os
from donorschoose import logger
from pathlib import Path
from donorschoose.utils.common import read_csv
import numpy as np
from scipy.sparse import coo_matrix
from sklearn.linear_model import LogisticRegression
from donorschoose.entity.config_entity import (ModelTrainingConfig)
import joblib

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        self.X_train=None
        self.y_train = None
    def read_files(self):
        '''
        Fetches data from the specified URLs and returns DataFrames.
        '''
        try: 
            root_dir = self.config.root_dir
            os.makedirs(root_dir, exist_ok=True)         
            train_file_path = Path(self.config.local_train_file)          
            train_data = np.load(train_file_path)
            sparse_matrix = coo_matrix((train_data['data'], (train_data['row'], train_data['col'])), shape=train_data['shape'])

            sparse_matrix = sparse_matrix.tocsr()
 
            self.X_train = sparse_matrix[:, :-1].toarray() 
            self.y_train = sparse_matrix[:, -1].toarray().flatten()   

            logger.info(f"Shape of X_train: {self.X_train.shape}")
            logger.info(f"Shape of y_train: {self.y_train.shape}")

        except Exception as e:
            raise e

    def train_log_reg(self):
        logreg = LogisticRegression(
                penalty=self.config.penalty,
                C=self.config.C,
                max_iter=self.config.max_iter,
                solver=self.config.solver
                )
        logreg.fit(self.X_train, self.y_train)
        model_filename = Path(self.config.root_dir,"logistic_regression_model.pkl")
        joblib.dump(logreg, model_filename)
        logger.info(f"model saved succesfully {model_filename}")
        