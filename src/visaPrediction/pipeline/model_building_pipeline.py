from src.visaPrediction import logger
from src.visaPrediction.config import ConfigurationManager
from src.visaPrediction.components.model_building import ModelBuilding

STAGE_NAME = "Model building Stage"

class ModelBuildPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_train_config = config.get_model_train_config()
            model = ModelBuilding(model_train_config)
            model.build_model()
      
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelBuildPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e