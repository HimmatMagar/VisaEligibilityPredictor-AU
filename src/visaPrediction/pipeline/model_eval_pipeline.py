from src.visaPrediction import logger
from src.visaPrediction.config import ConfigurationManager
from src.visaPrediction.components.model_eval import ModelEval

STAGE_NAME = "Model Eval Stage"

class ModelEvalPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_eval_config = config.get_model_eval_config()
            model = ModelEval(model_eval_config)
            model.val_data()
      
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvalPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e