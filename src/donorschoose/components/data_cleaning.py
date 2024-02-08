import os
from donorschoose import logger
import re
import pandas as pd
from tqdm import tqdm
from donorschoose.entity.config_entity import DataCleanConfig
from donorschoose.utils.common import read_csv
class DataCleaning:
    def __init__(self, config: DataCleanConfig):
        self.config = config
        self.stopwords= ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"]

    def read_files(self) -> pd.core.frame.DataFrame:
        '''
        Fetches data from the specified URLs and returns DataFrames.
        '''
        try: 
            root_dir = self.config.root_dir
            os.makedirs(root_dir, exist_ok=True)

            train_path = self.config.local_data_trainfile
            resource_path = self.config.local_data_resourcefile
            train_df = read_csv(train_path)
            resource_df = read_csv(resource_path)

        except Exception as e:
            raise e

        return train_df, resource_df
    
    def clean_text_column(df_column :pd.core.frame.DataFrame , columnName : str  )-> pd.core.frame.DataFrame :
        """
        this function will remove Spaces and special char from text column
        
        if we have any Nan value then it will fill nan value with 
        whatever have max count category
        """
        df_column =df_column.str.replace(' ','_')
        df_column =df_column.str.replace(',','_')
        df_column =df_column.str.replace('.','')
        df_column =df_column.str.replace('-','_')
        df_column =df_column.str.replace('&','_')
        df_column =df_column.str.replace(' The ','')
        df_column =df_column.str.lower()
        df_column =df_column.str.replace('___','_')
        df_column =df_column.str.replace('__','_')
        
        max_count_id = df_column.value_counts().idxmax()
        df_column=df_column.fillna(max_count_id)
        
        logger.info(f"preprocessed column :{columnName} , unique categories Count : {len(df_column.value_counts())}")

        return df_column

    def decontracted(self ,phrase: str) -> str:
        # specific
        phrase = re.sub(r"won't", "will not", phrase)
        phrase = re.sub(r"can\'t", "can not", phrase)

        # general
        phrase = re.sub(r"n\'t", " not", phrase)
        phrase = re.sub(r"\'re", " are", phrase)
        phrase = re.sub(r"\'s", " is", phrase)
        phrase = re.sub(r"\'d", " would", phrase)
        phrase = re.sub(r"\'ll", " will", phrase)
        phrase = re.sub(r"\'t", " not", phrase)
        phrase = re.sub(r"\'ve", " have", phrase)
        phrase = re.sub(r"\'m", " am", phrase)
        
        return phrase

    def preprocess_text(self ,text_data: list)-> list:
        preprocessed_text = []
        for sentance in tqdm(text_data):
            sent = self.decontracted(sentance)
            sent = sent.replace('\\r', ' ')
            sent = sent.replace('\\n', ' ')
            sent = sent.replace('\\"', ' ')
            sent = re.sub('[^A-Za-z0-9]+', ' ', sent)
            sent = ' '.join(e for e in sent.split() if e.lower() not in self.stopwords)
            preprocessed_text.append(sent.lower().strip())
        return preprocessed_text
    