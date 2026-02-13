import os
import zipfile
import urllib.request as r
from src.visaPrediction import logger
from src.visaPrediction.entity import DataIngestonConfig

class DataIngeston:
      def __init__(self, config: DataIngestonConfig):
            self.config = config

      def download_file(self):
            if not os.path.exists(self.config.ziped_data_path):
                  filename, header = r.urlretrieve(
                        url = self.config.source_url,
                        filename=self.config.ziped_data_path
                  )
                  logger.info(f"{filename} download with fillowing {header}")
            else:
                  logger.info("file already exist")
            
      
      def unzip_file(self):
            file = self.config.unziped_file
            os.makedirs(file, exist_ok=True)
            with zipfile.ZipFile(self.config.ziped_data_path, 'r') as f:
                  f.extractall(file)