import joblib
from pathlib import Path


class PredictionPipeline:
      def __init__(self):
            self.model = joblib.load(Path('artifact/model_building/model.pkl'))

      def transform_user_input(self, data):
            import os

            if 'documents_submitted' not in data.columns:
                  raise ValueError("Missing required column: 'documents_submitted'")
            
            data['documents_submitted'] = (
                  data['documents_submitted']
                  .str.replace(',', ' ', regex=True)
                  .str.lower()
            )
            
            preprocessor_path = "artifact/data_transformation/preprocessor.pkl"
            if not os.path.exists(preprocessor_path):
                  raise FileNotFoundError(f"Preprocessor not found at {preprocessor_path}")
            
            preprocessor = joblib.load(preprocessor_path)
            transformed_data = preprocessor.transform(data)
            
            return transformed_data.tolist()

      def prediction(self, data):
            prediction = self.model.predict(data)
            return prediction