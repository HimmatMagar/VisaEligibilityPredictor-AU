from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestonConfig:
      root_dir: Path
      source_url: str
      ziped_data_path: Path
      unziped_file: Path


@dataclass
class DataValidationConfig:
      root_dir: Path
      status_file: Path
      file_path: str
      schema: dict


@dataclass
class DataTransformationConfig:
      root_dir: Path
      file_path: Path


@dataclass
class ModelBuildingConfig:
      root_dir: Path
      x_train_file_path: Path
      y_train_file_path: Path
      c: int
      gamma: str
      kernel: str
      model: str