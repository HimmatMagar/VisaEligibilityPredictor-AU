from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestonConfig:
      root_dir: Path
      source_url: str
      ziped_data_path: Path
      unziped_file: Path