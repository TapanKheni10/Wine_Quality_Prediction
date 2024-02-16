from WineQuality import logger
import pandas as pd
from WineQuality.entity import config_entity

class DataValidation:
    def __init__(self, config: config_entity.DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            data.drop(["Id"], axis=1, inplace=True)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise e