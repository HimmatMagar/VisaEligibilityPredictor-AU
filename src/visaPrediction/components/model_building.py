import os
import joblib
from pathlib import Path
from sklearn.svm import SVC
from src.visaPrediction import logger
from src.visaPrediction.utils import *
from src.visaPrediction.entity import ModelBuildingConfig


class ModelBuilding:
      def __init__(self, config: ModelBuildingConfig):
            self.config = config

      def build_model(self) -> None:
            x_train = load_file(Path(self.config.x_train_file_path))
            y_train = load_file(Path(self.config.y_train_file_path))

            model = SVC(
                  C=self.config.c,
                  gamma=self.config.gamma,
                  kernel=self.config.kernel
            )

            model.fit(x_train, y_train)

            model_path = os.path.join(self.config.root_dir, self.config.model)
            with open(model_path, "wb") as f:
                  joblib.dump(model, f)
            logger.info(f"Model building successfully in: {model}")
