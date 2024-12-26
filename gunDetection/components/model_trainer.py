import os, sys
import yaml
from gunDetection.logger import logging
from gunDetection.exception import AppException
from gunDetection.entity.config_entity import ModelTrainderConfig
from gunDetection.utils.main_utils import read_yam_file
from gunDetection.entity.artifacts_entity import ModelTrainerArtifacts
from ultralytics import YOLO

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainderConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            logging.info("Initiating model training")
            os.system("unzip data.zip")
            os.system("rm data.zip")

            
            model_config_file_name = self.model_trainer_config.pretrained_weight_name.split(".")[0]
            print(model_config_file_name)

            model = YOLO('jameslahm/yolov10s.pt')
            # train if you have resources
            '''
            model.train(
                data = 'data.yaml',
                epochs = self.model_trainer_config.no_epochs,
                batch = self.model_trainer_config.batch_size,
                imgsz = 640,
                name = 'yolo_model',
                workers = 4
            )
            '''
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp /home/dpach/Documents/GUN_DETECTION/Gun-detection/best_model_wts/best.pt {self.model_trainer_config.model_trainer_dir}/")
            model_trainer_artifacts = ModelTrainerArtifacts(
                # store the path of the trained model weights
                trained_model_path="/home/dpach/Documents/GUN_DETECTION/Gun-detection/best_model_wts/best.pt"
            )
            logging.info(f"Model weights savedf saved at {model_trainer_artifacts.trained_model_path}")
            return model_trainer_artifacts
        except Exception as e:
            raise AppException(e, sys)