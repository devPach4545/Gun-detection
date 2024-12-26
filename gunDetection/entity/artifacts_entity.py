from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    data_zip_file_path: str
    feature_store_file_path: str

@dataclass
class DataValidationArtifacts:
    val_status: bool

@dataclass
class ModelTrainerArtifacts:
    trained_model_path: str