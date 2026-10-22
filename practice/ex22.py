def box_size(box):
    x1,y1,x2,y2=box
    return x2-x1,y2-y1

width=box_size((100,50,180,200))

print(width)