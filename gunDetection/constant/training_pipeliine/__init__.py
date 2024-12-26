# Data ingestion
ARTIFACTS_DIR: str = "artifacts"

DATA_INGESTION_DIR: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1zd2yFehwEtZ5DHJUEXGcQUST1_LXPDk1/view?usp=sharing"


# Data Validation
DATA_VALIDATION_DIR: str = "data_validation"

DATA_VALIDATION_STATUS_FILE: str = "validation_status.txt"

DATA_VALIDATION_REQUIRED_FILES = ["train", "val", "data.yaml"]

# Model Trainer
MODEL_TRAINER_DIR: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolo10s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 80

MODEL_TRAINER_BATCH_SIZE: int = 16