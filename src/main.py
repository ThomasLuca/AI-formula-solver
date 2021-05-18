import warnings
warnings.filterwarnings('ignore')
from camera import Camera
from extractChars import Extractor
from predictor import Predictor
from calculator import Calculator

camera = Camera(600, 140)
imgBinary = camera.takeImage()

extractor = Extractor(imgBinary)
contours = extractor.getContours()
digits = extractor.extract(contours)

predictor = Predictor(digits)
predictor.predictCharacters()
predictionResults = predictor.getResults()

calculator = Calculator(predictionResults)
calculator.calculateX()
