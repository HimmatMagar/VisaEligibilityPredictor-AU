import joblib
from pathlib import Path


class PredictionPipeline:
      def __init__(self):
            self.model = joblib.load(Path('artifacts/model_building/model.pkl'))
      
      def prediction(self, data):
            prediction = self.model.predict(data)
            return prediction