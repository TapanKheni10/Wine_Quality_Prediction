from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.data_validation import DataValidation
from WineQuality import logger

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        obj = DataValidation(config=data_validation_config)
        obj.validate_all_columns()

if __name__ == '__main__':
    pass