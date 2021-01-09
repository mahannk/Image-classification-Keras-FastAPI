from tensorflow.keras.applications.nasnet import NASNetMobile, preprocess_input, decode_predictions
import numpy as np
import cv2

predictor = None

def init_predictor():
    return NASNetMobile()


def load_image(image):
    img = np.fromstring(image, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    img = np.expand_dims(img, 0)
    return img       
    
def predict(image):
    if predictor is None:
        predictor = init_predictor()
    
    img = preprocess_input(image)
    preds = decode_predictions(self.predictor.predict(img), 10)[0]

    results = {}
    for pred in preds:
        results.update({pred[1] : f"{pred[2] * 100:.2f}%"})   

# class Prediction:

#     def __init__(self):
#         self.model = NASNetMobile()
    
#     @staticmethod
#     def load_image(image):
#         img = np.fromstring(image, np.uint8)
#         img = cv2.imdecode(img, cv2.IMREAD_COLOR)
#         img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
#         img = np.expand_dims(img, 0)
#         return img     

#     def predict(self, image):
#         img = preprocess_input(image)
#         preds = decode_predictions(self.model.predict(img), 10)[0]

#         results = {}
#         for pred in preds:
#             results.update({pred[1] : f"{pred[2] * 100:.2f}%"})


#         return results
