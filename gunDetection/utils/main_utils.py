from gunDetection.exception import AppException
import sys
import os.path
import yaml
import base64



def read_yam_file(file_path: str) -> dict:
    try:
        with open('file_path', 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise AppException(e, sys) from e
    
def write_yam_file(file_path: str, content: object, replace: bool) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open('file_path', 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise AppException(e, sys) from e
    
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(imagePath):
    with open(imagePath, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
