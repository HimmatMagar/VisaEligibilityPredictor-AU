from src.visaPrediction import logger
from src.visaPrediction.pipeline.model_building_pipeline import ModelBuildPipeline
from src.visaPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.visaPrediction.pipeline.data_validation_pipeline import DataValidationPipeline
from src.visaPrediction.pipeline.data_transformation_pipeline import DataTransformationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Data Validation Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataValidationPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Data Transformation Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataTransformationPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Model building Stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = ModelBuildPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e