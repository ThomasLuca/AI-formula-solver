import cv2
import numpy as np

class Extractor:
    def __init__(self, imgBinary):
        self.imgBinary = imgBinary

    def getContours(self):
        contours,hierarchy = cv2.findContours(self.imgBinary, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        return contours

    
    def extract(self, contours):
        extractions = []
        for contour in contours:
            if cv2.contourArea(contour) > 30 and cv2.contourArea(contour) < 4000:
                [x,y,w,h] = cv2.boundingRect(contour)
                if  h>15 or w>15:
                    side = int(np.maximum(h, w))
                    xSquare = int(x + (w - side)/2)
                    ySquare = int(y + (h - side)/2)
                    # Roi = Region Of Interest
                    roi = self.imgBinary[ySquare:ySquare+side,xSquare:xSquare+side]
                    # MNIST images have digits in 20x20 centered in a 28x28 frame
                    roiSmall = cv2.resize(roi,(20, 20))
                    roiMargin = cv2.copyMakeBorder(roiSmall, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=[255,255,255])
                    extractions.append({ 
                        "x1": xSquare,
                        "y1": ySquare,
                        "x2": xSquare + side,
                        "y2": ySquare + side,
                        "side": side,
                        "img": roiMargin
                    })

        def sortX(e):
            return e["x1"]
        extractions.sort(key=sortX)
        return extractions
