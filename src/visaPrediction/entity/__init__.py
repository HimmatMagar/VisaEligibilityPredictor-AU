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