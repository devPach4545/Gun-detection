import os
import sys
import zipfile
import gdown
from gunDetection.entity.config_entity import DataIngestionConfig
from gunDetection.exception import AppException
from gunDetection.entity.artifacts_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)

    def download_data(self) -> str:
        try:
            url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            zip_file_path = os.path.join(zip_download_dir, "data.zip")

            file_id = url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_file_path)

            return zip_file_path
        except Exception as e:
            raise AppException(e, sys) 

    def unzip_dat(self, zip_file_path: str) -> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(feature_store_path)
            return feature_store_path
        except Exception as e:
            raise AppException(e, sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.unzip_dat(zip_file_path)

            data_ingestion_artifacts = DataIngestionArtifacts(
                data_zip_file_path=zip_file_path,
                feature_store_file_path=feature_store_path
            )

            return data_ingestion_artifacts
        except Exception as e:
            raise AppException(e, sys)

