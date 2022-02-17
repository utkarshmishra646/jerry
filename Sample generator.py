import cv2
import cv2module

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

detector = cv2.CascadeClassifier("C:\Python 3.10\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")


face_id = input("Enter a Numeric user ID here:  ")

print("Taking samples, look at camera ..........")
count = 0

while True:

    ret, img = cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count +=1


        cv2.imwrite("C:\\Users\\91930\\PycharmProjects\\pythonProject1\\python\\sample" +str(face_id)+ '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])

        cv2.imshow('image', img)


    k = cv2.waitKey(100) & 0xff
    if k==27: #press esc to stop
        break
    elif count >= 10:
        break

