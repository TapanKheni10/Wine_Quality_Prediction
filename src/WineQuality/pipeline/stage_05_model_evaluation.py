from WineQuality.components.model_evaluation import ModelEvaluation
from WineQuality.config.configuration import ConfigurationManager
from WineQuality import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        obj = ModelEvaluation(model_evaluation_config)
        obj.save_matrix()

if __name__ == '__main__':
    pass