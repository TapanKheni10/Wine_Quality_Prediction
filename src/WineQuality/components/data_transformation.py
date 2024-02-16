import os
from WineQuality import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from WineQuality.entity import config_entity

class DataTransformation:
    def __init__(self, config: config_entity.DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)
        data.drop(["Id"], axis=1, inplace=True)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted the data into train and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)