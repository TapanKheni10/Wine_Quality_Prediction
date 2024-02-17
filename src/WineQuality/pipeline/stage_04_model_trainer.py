from WineQuality.components.model_trainer import ModelTrainer
from WineQuality.config.configuration import ConfigurationManager
from WineQuality import logger

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        obj = ModelTrainer(config=model_trainer_config)
        obj.train()

if __name__ == '__main__':
    pass