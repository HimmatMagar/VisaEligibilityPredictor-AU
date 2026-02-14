import os
import joblib
import pandas as pd
from src.visaPrediction import logger
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from src.visaPrediction.entity import DataTransformationConfig
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder


class DataTransformation:
      def __init__(self, config: DataTransformationConfig):
            self.config = config


      def clean_data(self):
            df = pd.read_csv(self.config.file_path)

            df.drop(columns='rejection_reason', inplace=True)

            df['documents_submitted'] = df['documents_submitted'].str.replace(',', ' ', regex=True).str.lower()
            return df


      def transform_data(self):
            df = self.clean_data()

            encoder = LabelEncoder()
            df['visa_granted'] = encoder.fit_transform(df['visa_granted'])

            X = df.drop(columns='visa_granted')
            y = df['visa_granted']

            categorical_features = ['gender', 'visa_type']

            preprocessor = ColumnTransformer(
                  transformers= [
                        ('text', TfidfVectorizer(), 'documents_submitted'),
                        ('num', StandardScaler(), ['age']),
                        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
                  ]
            )
            x = preprocessor.fit_transform(X)
            y = df['visa_granted']

            return x, y
      
      
      def split_data(self):
            x, y = self.transform_data()

            x_train, x_val, y_train, y_val = train_test_split(
                  x,
                  y,
                  test_size=0.3
            )

            joblib.dump(x_train, os.path.join(self.config.root_dir, "x_train.pkl"))
            joblib.dump(x_val, os.path.join(self.config.root_dir, "x_val.pkl"))
            joblib.dump(y_train, os.path.join(self.config.root_dir, "y_train.pkl"))
            joblib.dump(y_val, os.path.join(self.config.root_dir, "y_val.pkl"))

            logger.info("Split data successfully")