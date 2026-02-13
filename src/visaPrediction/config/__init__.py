from src.visaPrediction.utils import *
from src.visaPrediction.entity import *
from src.visaPrediction.constants import *


class ConfigurationManager:
      def __init__(
            self,
            config = CONFIG_FILE_PATH,
            schema = SCHEMA_FILE_PATH,
            params = PARAMS_FILE_PATH
      ):
            self.config = load_yaml_file(config)
            self.schema = load_yaml_file(schema)
            self.params = load_yaml_file(params)

            create_directory([self.config.artifact_root])
      
      def get_data_ingestion_configuration(self) -> DataIngestonConfig:
            config = self.config.data_ingestion

            create_directory([config.root_dir])

            data_ingestion_config = DataIngestonConfig(
                  root_dir=config.root_dir,
                  source_url=config.source_url,
                  ziped_data_path=config.ziped_data_path,
                  unziped_file=config.unziped_file
            )
            return data_ingestion_config