import cv2, os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path + '\mouth.xml'

mouthDetect = cv2.CascadeClassifier(dir_path)
cam = cv2.VideoCapture(0)

while (True):
    ret, img = cam.read()
    if ret is True:
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mouths = mouthDetect.detectMultiScale(grayImg, 1.3, 5)

        for (x, y, w, h) in mouths:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.waitKey(80)

        cv2.imshow("Camera", img)
        # cv2.waitKey(1)

        if cv2.waitKey(1) == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()
