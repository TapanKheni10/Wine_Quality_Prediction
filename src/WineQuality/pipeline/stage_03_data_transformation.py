from WineQuality.config.configuration import ConfigurationManager
from WineQuality.components.data_transformation import DataTransformation
from WineQuality import logger
from pathlib import Path

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                obj = DataTransformation(config=data_transformation_config)
                obj.train_test_split()

            else:
                raise Exception("Your data in not in the correct format.")
    
        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == '__main__':
    pass