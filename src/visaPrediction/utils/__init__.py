import os
import yaml
import json
from pathlib import Path
from box.config_box import ConfigBox
from src.visaPrediction import logger
from ensure import ensure_annotations
from box.exceptions import BoxValueError


@ensure_annotations
def load_yaml_file(yaml_file: Path) -> ConfigBox:
      try:
            with open(yaml_file) as f:
                  content = yaml.safe_load(f)
                  logger.info(f"yaml file: {yaml_file} loaded successfully")
                  return ConfigBox(content)
      except BoxValueError:
            raise ValueError("Yaml file is empty")
      except Exception:
            raise Exception


@ensure_annotations
def create_directory(list_directory: list, verbose=True):
      for filename in list_directory:
            os.makedirs(filename, exist_ok=True)

            if verbose:
                  logger.info(f"File directory: {filename} created successfully")


@ensure_annotations
def save_json(path: Path, data: dict):
      with open(path, 'w') as f:
            json.dump(data, f, indent=4)
      logger.info(f"json file: {path} saved successfully")
