import cv2
import time
import os
import hand as htm
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate('Firebase-SDK.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hand-opencv-esp-default-rtdb.firebaseio.com/'
})
songontay = 0
pTime = 0
cap = cv2.VideoCapture(0)
ref = db.reference('Control')
FolderPath = r"D:\Python_DA2\Hand\Fingers"
lst = os.listdir(FolderPath)
lst_2 = []
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    print(f"{FolderPath}/{i}")
    lst_2.append(image)
print(lst_2[0].shape)
detector = htm.handDetector(detectionCon=1)
fingerid = [4, 8, 12, 16, 20]
while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)  # phat hien vi tri tay
    if len(lmList) != 0:
        fingers = []
        # viet cho ngon cai - diem 4 so voi diem 3
        if lmList[fingerid[0]][1] < lmList[fingerid[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # viet cho 4 ngon dai
        for id in range(1, 5):
            if lmList[fingerid[id]][2] < lmList[fingerid[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # dem so ngon tay
        songontay = fingers.count(1)
    # chen hinh ngon tay
    h, w, c = lst_2[songontay - 1].shape
    frame[0:h, 0:w] = lst_2[songontay - 1]
    # ve hinh hien thi so ngon tay
    cv2.rectangle(frame, (0, 200), (150, 400), (0, 255, 255), -1)
    cv2.putText(frame, str(songontay), (25, 350), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 0), 5)
    # viet ra fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # show thoi gian fps len man hinh
    cv2.putText(frame, f"FPS:  {int(fps)}", (150, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
    #  gui du lieu len Firebase
    if songontay == 1:
        ref.update({
            'LED': 1
        })

    if songontay == 2:
        ref.update({
            'LED': 0
        })

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord("q"):  # do tre 1/1000 s, neu bam q se thoat
        break 
cap.release()  # giai phong camera
cv2.destroyAllWindows()  # thoat tat ca cac cua so