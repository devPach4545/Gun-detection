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

@dataclass
class DataValidationConfig:
    data_val_dir: str = os.path.join(
        training_pipe_config.artifacts_dir, DATA_VALIDATION_DIR
    )

    data_val_status_file: str = os.path.join(
        data_val_dir, DATA_VALIDATION_STATUS_FILE
    )

    data_val_required_files = DATA_VALIDATION_REQUIRED_FILES

@dataclass
class ModelTrainderConfig:
    model_trainer_dir: str = os.path.join(
        training_pipe_config.artifacts_dir, MODEL_TRAINER_DIR
    )

    pretrained_weight_name: str = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    no_epochs: int = MODEL_TRAINER_NO_EPOCHS

    batch_size: int = MODEL_TRAINER_BATCH_SIZE