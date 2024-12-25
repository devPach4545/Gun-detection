import sys, os
from gunDetection.logger import logging
from gunDetection.exception import AppException
from gunDetection.entity.config_entity import DataIngestionConfig
from gunDetection.components.data_ingestion import DataIngestion
from gunDetection.entity.artifacts_entity import DataIngestionArtifacts

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            logging.info("Initiating data ingestion")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed")
            return data_ingestion_artifacts
        except Exception as e:
            raise AppException(e, sys)
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            

        except Exception as e:
            raise AppException(e, sys)