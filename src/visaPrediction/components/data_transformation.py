import os
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from src.visaPrediction import logger
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from src.visaPrediction.utils.common import DataCleaner
from sklearn.feature_extraction.text import TfidfVectorizer
from src.visaPrediction.entity import DataTransformationConfig
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder


class DataTransformation:
      def __init__(self, config: DataTransformationConfig):
            self.config = config


      def transform_data(self):
            df = pd.read_csv(self.config.file_path)

            x = df.drop(columns='visa_granted')
            y = df['visa_granted']

            x_train, x_val, y_train, y_val = train_test_split(
                  x,
                  y,
                  test_size=0.3
            )

            encoder = LabelEncoder()
            y_train_encode = encoder.fit_transform(y_train)
            y_val_encode = encoder.transform(y_val)

            # Assuming x has columns: age (0), gender (1), visa_type (2), documents_submitted (3)
            preprocessor = Pipeline([
                  ('cleaner', DataCleaner()),
                  ('transformer', ColumnTransformer(
                        transformers= [
                              ('text', TfidfVectorizer(), 3),  # documents_submitted
                              ('num', StandardScaler(), [0]),  # age
                              ('cat', OneHotEncoder(handle_unknown='ignore'), [1, 2])  # gender, visa_type
                        ]
                  ))
            ])
            
            x_train_transformed = preprocessor.fit_transform(x_train)
            x_val_transformed = preprocessor.transform(x_val)
            joblib.dump(preprocessor, os.path.join(self.config.root_dir, 'preprocessor.pkl'))

            joblib.dump(x_train_transformed, os.path.join(self.config.root_dir, "x_train.pkl"))
            joblib.dump(x_val_transformed, os.path.join(self.config.root_dir, "x_val.pkl"))
            joblib.dump(y_train_encode, os.path.join(self.config.root_dir, "y_train.pkl"))
            joblib.dump(y_val_encode, os.path.join(self.config.root_dir, "y_val.pkl"))

            logger.info("Split data successfully")