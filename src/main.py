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

predictor = Predictor(digits)
predictor.predictCharacters()
predictionResults = predictor.getResults()

calculate = Calculate()
print (calculate.calcroots(predictionResults))
