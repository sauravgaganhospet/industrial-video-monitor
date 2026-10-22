def box_width(box):
    x1,y1,x2,y2= box
    return x2-x1

w=box_width((100,50,180,200))
print(w)

def hello(num):
    x=2+num
    return x*2

print(hello(2))