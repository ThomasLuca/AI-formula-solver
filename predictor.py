import warnings
warnings.filterwarnings('ignore')
import cv2
import numpy as np
from keras.models import load_model

class Predictor:
    def __init__(self):
        self.model = load_model('./digit_recognizer.h5')
    
    def format_image(self, img):
            img = cv2.resize(img, (28, 28), interpolation = cv2.INTER_AREA)
            img = np.array(img)
            img = img.astype(np.float32).reshape(-1, 784)
            img = 255 - img
            img /= 255
            return img
    
    def predict(self, img):
        formatted = self.format_image(img)
        certainty = self.model.predict(formatted)[0]
        classes = certainty
        sorted = np.sort(certainty)[::-1]
        digit = np.where(classes == sorted[0])[0][0]
        return (digit, round(sorted[0]*100, 2))