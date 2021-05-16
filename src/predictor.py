import warnings
warnings.filterwarnings('ignore')
import cv2
import numpy as np
from keras.models import load_model

class Predictor:
    def __init__(self, digits):
        self.model = load_model('./digit_recognizer.h5')
        self.digits = digits
        self.predicted = []
    
    def format_image(self, img):
        img = cv2.resize(img, (28, 28), interpolation = cv2.INTER_AREA)
        img = np.array(img)
        img = img.astype(np.float32).reshape(-1, 784)
        img = 255 - img
        img /= 255
        return img
    
    def predictCharacters(self):
        index = 0
        for digit in self.digits:
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
            
            if self.isValidExtraction(result, index):
                self.predicted.append(result)
                height = digit["side"]
                print(f"{result} : {round(sorted[0]*100, 2)}% - {height}")

                cv2.imshow("single", digit["img"])
                key = cv2.waitKey(0)
            index += 1

    def isSquare(self, digit):
        if len(self.predicted) and self.predicted[-1] == "X" and digit["side"] < 40:
            return True
        return False
    
    # Avoid recognizing inner contour of digit as separate digit
    def isValidExtraction(self, result, index):
        if result == 2 or self.digits[index]["side"] > 45 or not index:
            return True
        elif self.digits[index]["x1"] >= self.digits[index-1]["x1"] and self.digits[index]["x2"] <= self.digits[index-1]["x2"]:
            return False
        return True
    
    def getResults(self):
        return self.predicted
        
