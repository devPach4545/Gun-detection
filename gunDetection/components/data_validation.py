import os
import shutil
import sys
import zipfile
import gdown
from gunDetection.entity.config_entity import DataIngestionConfig, DataValidationConfig
from gunDetection.exception import AppException
from gunDetection.entity.artifacts_entity import DataIngestionArtifacts, DataValidationArtifacts

class DataValidation:
    def __init__(self, data_ingestion_artifacts: DataIngestionArtifacts, 
                 data_validation_config: DataValidationConfig = DataValidationConfig()):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e, sys)
        
    def val_all_files(self) -> bool:
        try:
            val_status = None
            all_files = os.listdir(self.data_ingestion_artifacts.feature_store_file_path)
            # log all files
            print(self.data_ingestion_artifacts.feature_store_file_path)
            for file in all_files:
                if file not in self.data_validation_config.data_val_required_files:
                    val_status = False
                    os.makedirs(self.data_validation_config.data_val_dir, exist_ok=True)
                    with open(self.data_validation_config.data_val_status_file, "w") as f:
                        f.write("false")
                else:
                    val_status = True
                    os.makedirs(self.data_validation_config.data_val_dir, exist_ok=True)
                    with open(self.data_validation_config.data_val_status_file, "w") as f:
                        f.write("true")
                return val_status
        except Exception as e:
            raise AppException(e, sys)
        

    def initiate_data_val(self) -> DataValidationArtifacts:
        try:
            val_status = self.val_all_files()
            data_validation_artifacts = DataValidationArtifacts(val_status=val_status)

            if val_status:
                shutil.copy(self.data_ingestion_artifacts.data_zip_file_path, os.getcwd())
            return data_validation_artifacts
        except Exception as e:
            raise AppException(e, sys)