# Motivation and Goals
- There are several gun-related crimes happening in the USA. So, I attempted to make a website using yolov10, which is a robust computer vision algorithm that can detect objects with laser precision.
- Another goal of mine to make this web-app is to learn how CI/CD pipeline, Docker, and AWS works. I deployed the project on AWS using EC2 and ECR, since I don't have a premium subscription, I had to take it down.
# DEMO
- video link
# Tech Stacks
- Vanila JS for frontend
- Flask for backend
# Machine learning pipeline
- There are three main components
1. Data Ingestion
2. Data Validation
3. Model Trainer
# Running on local machine
1. you should clone the repo using `https://github.com/devPach4545/Gun-detection.git` and go to the Gun-detection dir
2. Create an anaconda or a virtual environment
3. Use `pip install -r requirements.txt` to install the dependencies
4. In your command line, type `python app.py` and run the application.
5. Also, make sure you use the avaliable port and host for your flask app.
6. Show the video above to detect a gun
# Note:
1. I do not have an access to a strong gpu, therefore I have trained the model for only 80 epochs, which is why you may not see a remarkable accuracy.
# Results
- ![image](https://github.com/user-attachments/assets/e7636294-cff8-4e77-b0f7-fde7a40e6ae2)

