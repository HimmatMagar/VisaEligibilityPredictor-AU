import joblib
from src.visaPrediction import logger
from src.visaPrediction.config import ConfigurationManager
from src.visaPrediction.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline():
      def __init__(self):
            pass


      def main(self):
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transform = DataTransformation(data_transformation_config)
            data_transform.split_data()
      
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataTransformationPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e
      