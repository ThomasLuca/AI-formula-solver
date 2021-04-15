import cv2

class Camera:
    def __init__(self, roiWidth, roiHeight):
        self.cap = cv2.VideoCapture(0)
        self.coordinates = self.setRoi(roiWidth, roiHeight)
        

    def setRoi(self, roiWidth, roiHeight):
        capWidth = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        capHeight = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        xStart = int((capWidth - roiWidth) / 2)
        xEnd = int(xStart + roiWidth)
        yStart = int((capHeight - roiHeight) / 2)
        yEnd = int(yStart + roiHeight)
        return {
            "xStart": xStart,
            "xEnd": xEnd,
            "yStart": yStart,
            "yEnd": yEnd
        }

    def takeImage(self):
        if self.cap.isOpened():
            rval, frame = self.cap.read()
        else:
            rval = False

        imgNr = 1
        while rval:
            cv2.imshow('Webcam',frame)
            rval, frame = self.cap.read()
            key = cv2.waitKey(20)
            if key == 49: # Nr 1, take a Photo
                img = "img_{}.png".format(imgNr)
                frame = frame[self.coordinates["yStart"]: self.coordinates["yEnd"], self.coordinates["xStart"]: self.coordinates["xEnd"]]
                cv2.imwrite(img, frame)
                img2 = cv2.imread('./' + img,  cv2.IMREAD_ANYDEPTH)
                ret, imgBinary = cv2.threshold(img2, 120, 255, cv2.THRESH_BINARY)
                cv2.imwrite(img, imgBinary)
                imgNr += 1
                return imgBinary
            elif key == 27 : # Esc, exit
                break
            else:
                self.drawRectangle(frame)
        self.deactivateCap()
    
    
    def drawRectangle(self, frame):
        cv2.rectangle(
            img=frame,
            pt1=(self.coordinates["xStart"], self.coordinates["yStart"]),
            pt2=(self.coordinates["xEnd"], self.coordinates["yEnd"]),
            color=(0, 255, 0),
            thickness=1,
            lineType=8,
            shift=0
        )

    
    def deactivateCap(self):
        self.cap.release()
        cv2.destroyAllWindows()
