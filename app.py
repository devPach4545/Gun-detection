from gunDetection.logger import logging
from gunDetection.exception import AppException
import sys
from gunDetection.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()
