import cv2
import pyfakewebcam
from skimage.transform import resize

cap = cv2.VideoCapture('/dev/video0')
height, width = 480, 640
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)
fake = pyfakewebcam.FakeWebcam('/dev/video2', width, height)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)    
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    fake.schedule_frame(frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()