import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from WineQuality.utils.common import save_json
from urllib.parse import urlparse
import numpy as np
import joblib
from WineQuality.entity.config_entity import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_matrix(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true=y_true, y_pred=y_pred))
        mse = mean_squared_error(y_true=y_true, y_pred=y_pred)
        r2 = r2_score(y_true=y_true, y_pred=y_pred)
        return rmse, mse, r2
    
    def save_matrix(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        y_pred = model.predict(X_test)

        (rmse, mse, r2) = self.eval_matrix(y_true=y_test, y_pred=y_pred)

        scores = {"rmse": rmse, "mse": mse, "r2_score": r2}
        save_json(path=Path(os.path.join(self.config.root_dir, self.config.metric_name)), data=scores)
