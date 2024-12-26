import sys, os
from gunDetection.pipeline.training_pipeline import TrainingPipeline
from gunDetection.utils.main_utils import decodeImage, encodeImage
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from gunDetection.logger import logging
from gunDetection.constant.application import *



app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputimg.jpg"

@app.route("/train")
def trainRoute():
    obj = TrainingPipeline()
    obj.run_pipeline()
    return "Training Completed"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
@cross_origin()
def predictRoute():
    try:
        logging.info("Getting image as JSON")
        image = request.json['image']
        decodeImage(image, CLIENT.filename)
        logging.info("Image decoded")

        logging.info("Predicting image")
        os.system("yolo detect predict model=/home/dpach/Documents/GUN_DETECTION/Gun-detection/artifacts/model_trainer/best.pt source=/home/dpach/Documents/GUN_DETECTION/Gun-detection/data/inputimg.jpg")
        
        logging.info("Encoding image")
        encodedImg = encodeImage("/home/dpach/Documents/GUN_DETECTION/Gun-detection/runs/detect/predict/inputimg.jpg")
        logging.info("Image prediction completed and returning the result")

        result = {"image": encodedImg}
        os.system("rm -rf /home/dpach/Documents/GUN_DETECTION/Gun-detection/runs/detect")
    
    
    except ValueError as e:
        return Response(e.args[0], status=400)
    except KeyError as e:
        return Response("Provide image in the request", status=400)
    except Exception as e:
        import traceback
        traceback.print_exc()  # Log the full stack trace for debugging
        return Response(str(e), status=500)
    return jsonify(result)

if __name__ == "__main__":
    CLIENT = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
    # test encode
    
