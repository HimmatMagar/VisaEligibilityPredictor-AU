from src.visaPrediction import logger
from src.visaPrediction.config import ConfigurationManager
from src.visaPrediction.components.data_ingestion import DataIngeston

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_configuration()
            data_ingestion = DataIngeston(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_file()
      
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e