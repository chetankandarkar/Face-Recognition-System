from cv2 import cv2

def generate_dataset(img, id, img_id):
    cv2.imwrite("data1/user." + str(id) + "." + str(img_id) + ".jpg", img)


def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    for (x, y, w, h) in features:

        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        id, _ = clf.predict(gray_img[y:y + h, x:x + w])
        if id == 1:
            cv2.putText(img, "Chetan Kandarkar", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2,cv2.LINE_AA)
        elif id == 2:
            cv2.putText(img, "Naredra Modi", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        elif id == 3:
            cv2.putText(img, "Sachin Tendulkar", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        elif id == 4:
            cv2.putText(img, "Vidya Balan", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, "Unknown", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

        coords = [x,y,w,h]

    return coords


def recognize(img, clf, faceCascade):
    coords = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
    return img


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier1.yml")


def detect(img, faceCascade, img_id):
    # color = ("blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255))
    coords, img = draw_boundary(img, faceCascade, 1.3, 6, (0, 255, 0), "Face", clf)
    if len(coords) == 4:
        roi_img = img[coords[1]:coords[1] + coords[3], coords[0]:coords[0] + coords[2]]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)
    return img


video_capture = cv2.VideoCapture(0)

# img_id = 0

while True:
        ret, img = video_capture.read()
        # img = detect(img,faceCascade,img_id)
        img = recognize(img, clf, faceCascade)
        cv2.imshow("Face detection started stand infront of camera ", img)
        # img_id += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()