import cv2

cap = cv2.VideoCapture("data/line1.mp4")
cap.set(cv2.CAP_PROP_POS_FRAMES, 122)
ok, frame=cap.read()
cap.release()

height, width=frame.shape[:2]

for x in range(0, width, 100):
    cv2.line(frame, (x,0),(x,height),(0,255,255),1)
    cv2.putText(frame,str(x),(x+2,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

for y in range(0, height, 100):
    cv2.line(frame, (0,y),(width, y),(0,255,255),1)
    cv2.putText(frame,str(y), (2,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

cv2.imwrite("data/grid.png",frame)