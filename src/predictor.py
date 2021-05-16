import warnings
warnings.filterwarnings('ignore')
import cv2
import numpy as np
from keras.models import load_model

class Predictor:
    def __init__(self):
        self.model = load_model('../chars/digit_recognizer.h5')
        self.predicted = []
    
    def format_image(self, img):
        img = cv2.resize(img, (28, 28), interpolation = cv2.INTER_AREA)
        img = np.array(img)
        img = img.astype(np.float32).reshape(-1, 784)
        img = 255 - img
        img /= 255
        return img
    
    def predictCharacters(self, digits):
        for digit in digits:
            formatted = self.format_image(digit["img"])
            certainty = self.model.predict(formatted)[0]
            classes = certainty
            sorted = np.sort(certainty)[::-1]
            result = np.where(classes == sorted[0])[0][0]
            if result == 11:
                result = "X"
            if result == 10:
                result = "+"
            if result == 12:
                result = "-"

            if(result == 2 and self.isSquare(digit)):
                result = "²"                
            
            self.predicted.append(result)
            print(f"{result} : {round(sorted[0]*100, 2)}%")
            
            cv2.imshow("single", digit["img"])
            key = cv2.waitKey(0)

    def isSquare(self, digit):
        if self.predicted[-1] == "X" and digit["height"] < 40:
            return True
        return False
