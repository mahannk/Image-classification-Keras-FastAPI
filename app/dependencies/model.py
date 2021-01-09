from tensorflow.keras.applications.nasnet import NASNetMobile, preprocess_input, decode_predictions
import numpy as np
import cv2
from io import BytesIO
from PIL import Image

__model = None

def set_predictor():
    __model = NASNetMobile()
    return __model


def load_image(image):
    # img = np.fromstring(image, np.uint8)
    # img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    # img = np.expand_dims(img, 0)
    # return img      
    img = Image.open(BytesIO(image)) 
    img = np.asarray(img.resize((224, 224)))[..., :3]
    img = np.expand_dims(img, 0)
    return img
    
def classify_image(image):
    print('==============================================')
    global __model
    if __model is None:
        __model = set_predictor()
    
    img = preprocess_input(image)
    preds = decode_predictions(__model.predict(img), 10)[0]

    results = {}
    for pred in preds:
        results.update({pred[1] : f"{pred[2] * 100:.2f}%"})   

    return results

class Prediction:

    def __init__(self):
        self.model = NASNetMobile()
    
    @staticmethod
    def load_image(image):
        img = np.fromstring(image, np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)
        img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
        img = np.expand_dims(img, 0)
        return img     

    def predict(self, image):
        img = preprocess_input(image)
        preds = decode_predictions(self.model.predict(img), 10)[0]

        results = {}
        for pred in preds:
            results.update({pred[1] : f"{pred[2] * 100:.2f}%"})


        return results
