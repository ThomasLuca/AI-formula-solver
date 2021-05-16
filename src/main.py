import warnings
warnings.filterwarnings('ignore')
import cv2
from camera import Camera
from extractChars import Extractor
from predictor import Predictor

camera = Camera(600, 140)
imgBinary = camera.takeImage()

extractor = Extractor(imgBinary)
contours = extractor.getContours()
digits = extractor.extract(contours)

predictor = Predictor()
predictor.predictCharacters(digits)


# for digit in digits:
#     print(predictor.predictCharacters(digit["img"]))
#     cv2.imshow("single", digit["img"])
#     key = cv2.waitKey(0)

