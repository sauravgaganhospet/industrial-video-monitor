def box_center(box):
    x1,y1,x2,y2=box
    a=(x1+x2)//2
    b=(y1+y2)//2
    return a, b

cx, cy=box_center((100,50,180,200))
print(f"The centre coordinates are:({cx,cy})")