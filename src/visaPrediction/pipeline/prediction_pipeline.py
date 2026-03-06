import joblib
from pathlib import Path


class PredictionPipeline:
      def __init__(self):
            self.model = joblib.load(Path('artifact/model_building/model.pkl'))
            self.preprocessor = joblib.load(Path('artifact/data_transformation/preprocessor.pkl'))

      def prediction(self, data):
            data_transformed = self.preprocessor.transform(data)
            prediction = self.model.predict(data_transformed)
            return prediction