import os
from donorschoose import logger
from pathlib import Path
from donorschoose.utils.common import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import FeatureHasher
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from scipy.sparse import save_npz
from scipy.sparse import hstack
from donorschoose.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.clean_df = None
        self.X_train = None
        self.y_train = None 
        self.X_val = None 
        self.y_val = None 
        self.X_test = None
        self.y_test = None
        self.X_train_transformed = None
        self.X_val_transformed =None
        self.X_test_transformed = None
        
    def read_files(self):
        '''
        Fetches data from the specified URLs and returns DataFrames.
        '''
        try: 
            root_dir = self.config.root_dir
            os.makedirs(root_dir, exist_ok=True)
            clean_data_path = Path(self.config.local_data_cleanfile)          
            self.clean_df = read_csv(clean_data_path)
            
        except Exception as e:
            raise e
        
    def split_data(self , columnName: str):
        X=self.clean_df.drop(columnName , axis=1)
        Y=self.clean_df[columnName]
        
        self.X_train , self.X_val  , self.y_train , self.y_val = train_test_split(X , Y , test_size=0.30 , stratify=Y)
        self.X_val ,self.X_test,self.y_val ,self.y_test= train_test_split(self.X_val , self.y_val , test_size=0.30 , stratify=self.y_val)
        logger.info(f"Data Split into Train val test")
        logger.info(f"Train data shape: {self.X_train.shape} , {self.y_train.shape}")
        logger.info(f"Val data shape: {self.X_val.shape} , {self.y_val.shape}")
        logger.info(f"test data shape: {self.X_test.shape} , {self.y_test.shape}")
    
    def tfIdef_text(self , columnName: str):
        tfidf_vectorizer = TfidfVectorizer(min_df =20 ,max_features=5000)
        self.X_train_transformed = tfidf_vectorizer.fit_transform(self.X_train[columnName])
        self.X_val_transformed = tfidf_vectorizer.transform(self.X_val[columnName])
        self.X_test_transformed = tfidf_vectorizer.transform(self.X_test[columnName])
        logger.info(f"{columnName} transformed to tfidf")
                
    def onehotencoding_feature(self , column_list: list):
        
        label_encoder = ColumnTransformer(
            transformers=[
                ('onehot',OneHotEncoder(handle_unknown='ignore'), ['teacher_prefix', 'school_state', 'project_grade_category'])
            ],
            remainder='passthrough'
        )   
        
        X_train_transformed_onehot = label_encoder.fit_transform(self.X_train[column_list])
        X_val_transformed_onehot = label_encoder.transform(self.X_val[column_list])
        X_test_transformed_onehot = label_encoder.transform(self.X_test[column_list])
        
        self.X_train_transformed = hstack([self.X_train_transformed , X_train_transformed_onehot])
        self.X_val_transformed = hstack([self.X_val_transformed , X_val_transformed_onehot])
        self.X_test_transformed = hstack([self.X_test_transformed , X_test_transformed_onehot])
        
        logger.info(f"features {column_list} transformed to Onehot encode features")
        logger.info(f"one hot encode features shape:{self.X_train_transformed.shape , self.X_val_transformed.shape, self.X_test_transformed.shape} ")
                
    def feature_hash(self , columnName : str , n_feature: int):
        self.X_train[columnName] = self.X_train[columnName].apply(lambda x: [x])
        self.X_test[columnName] = self.X_test[columnName].apply(lambda x: [x])
        self.X_val[columnName] = self.X_val[columnName].apply(lambda x: [x])
        
        hasher = FeatureHasher(n_features= n_feature, input_type="string", alternate_sign=False)
        X_train_hashed = hasher.fit_transform(self.X_train[columnName])
        X_val_hashed = hasher.transform(self.X_val[columnName])
        X_test_hashed = hasher.transform(self.X_test[columnName])  

        self.X_train_transformed = hstack([self.X_train_transformed , X_train_hashed])
        self.X_val_transformed = hstack([self.X_val_transformed , X_val_hashed])
        self.X_test_transformed = hstack([self.X_test_transformed , X_test_hashed])
                   
        logger.info(f"feature hash for {columnName} and number of features {n_feature}  ")
        logger.info(f"feature hash shape:{self.X_train_transformed.shape , self.X_val_transformed.shape, self.X_test_transformed.shape} ")
        
    def normalize_column(self ,columnName: str):
        try:
            scaler = StandardScaler()
            scaler.fit(self.X_train[columnName].values.reshape(-1, 1))
            X_train_normalized_feature=scaler.transform(self.X_train[columnName].values.reshape(-1, 1) )
            X_val_normalized_feature=scaler.transform(self.X_val[columnName].values.reshape(-1, 1) )
            X_test_normalized_feature=scaler.transform(self.X_test[columnName].values.reshape(-1, 1) )
            
            self.X_train_transformed = hstack([self.X_train_transformed ,X_train_normalized_feature])
            self.X_val_transformed = hstack([self.X_val_transformed ,X_val_normalized_feature])
            self.X_test_transformed = hstack([self.X_test_transformed , X_test_normalized_feature])
                    
            logger.info(f"Normalized feature for {columnName} ")
            logger.info(f"Normalized feature shape:{self.X_train_transformed.shape , self.X_val_transformed.shape, self.X_test_transformed.shape} ")
        
        except Exception as e:
            raise e

    def save_transformed_data(self):

        self.X_train_transformed = hstack([self.X_train_transformed ,self.y_train.values.reshape(-1, 1)])
        self.X_val_transformed = hstack([self.X_val_transformed ,self.y_val.values.reshape(-1, 1)])
        self.X_test_transformed = hstack([self.X_test_transformed , self.y_test.values.reshape(-1, 1)])
        local_dir_path = self.config.root_dir
        save_npz(Path(local_dir_path+"/train.npz"), self.X_train_transformed)
        save_npz(Path(local_dir_path+"/val.npz"), self.X_val_transformed)
        save_npz(Path(local_dir_path+"/test.npz"), self.X_test_transformed)


            