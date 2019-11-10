import cv2 
from pydarknet import Detector, Image
net = Detector(bytes("tank.cfg", encoding="utf-8"), bytes("tank.weights", encoding="utf-8"), 0, bytes("tank.data",encoding="utf-8"))

def Detect(path): 
      
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
  
    while success: 
  
        success, image = vidObj.read() 
        img_darknet = Image(image)
        results = net.detect(img_darknet)
        for cat, score, bounds in results:
           x, y, w, h = bounds
           cv2.rectangle(image, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)
           cv2.putText(image,str(cat.decode("utf-8")),(int(x),int(y)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))

        cv2.imshow("Detected Tank", image) 
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        count += 1
  
if __name__ == '__main__': 
    #Detect(path to the surveillance video)
    Detect("test.mp4") 
