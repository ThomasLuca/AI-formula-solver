import warnings
warnings.filterwarnings('ignore')
import cv2
from camera import Camera
from extractChars import Extractor
from predictor import Predictor
from calculate import Calculate

camera = Camera(600, 140)
imgBinary = camera.takeImage()

extractor = Extractor(imgBinary)
contours = extractor.getContours()
digits = extractor.extract(contours)

predictor = Predictor()
calculate = Calculate()


for digit in digits:
    number = predictor.predict(digit["img"])
    numbers.append(number)
    print(number)
    print(calculate.calcroots(numbers))
    cv2.imshow("single", digit["img"])
    key = cv2.waitKey(0)



