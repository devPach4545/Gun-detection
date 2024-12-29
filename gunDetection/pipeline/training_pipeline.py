import sys, os
from gunDetection.exception import AppException
from gunDetection.entity.config_entity import DataIngestionConfig, DataValidationConfig, ModelTrainderConfig
from gunDetection.components.data_ingestion import DataIngestion
from gunDetection.components.data_validation import DataValidation
from gunDetection.entity.artifacts_entity import DataIngestionArtifacts, DataValidationArtifacts, ModelTrainerArtifacts
from gunDetection.components.model_trainer import ModelTrainer
class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_val_config = DataValidationConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifacts
        except Exception as e:
            raise AppException(e, sys)
        
    def start_data_val(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataValidationArtifacts:
        try:
            data_val = DataValidation(data_ingestion_artifacts, self.data_val_config)
            data_val_artifacts = data_val.initiate_data_val()
            return data_val_artifacts
        except Exception as e:
            raise AppException(e, sys)


    def start_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            model_trainer_config = ModelTrainderConfig()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer_artifacts = model_trainer.initiate_model_trainer()
            return model_trainer_artifacts
        except Exception as e:
            raise AppException(e, sys)
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_val_artifacts = self.start_data_val(data_ingestion_artifacts=data_ingestion_artifacts)
            model_trainer_artifacts = self.start_model_trainer()
        except Exception as e:
            raise AppException(e, sys)
