import os
from datetime import datetime
from dataclasses import dataclass
from gunDetection.constant.training_pipeliine import *

@dataclass
class TrainingPipeConfig:
    artifacts_dir: str = ARTIFACTS_DIR


training_pipe_config = TrainingPipeConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(
        training_pipe_config.artifacts_dir, DATA_INGESTION_DIR
    )

    feature_store_file_path = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url = DATA_DOWNLOAD_URL