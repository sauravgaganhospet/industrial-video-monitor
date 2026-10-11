boxes = [(100, 50, 180, 200), (300, 60, 340, 120), (500, 40, 620, 210)]

for box in boxes:
    x1,y1,x2,y2 = box
    width = x2-x1

    if width>50:
        print(box)