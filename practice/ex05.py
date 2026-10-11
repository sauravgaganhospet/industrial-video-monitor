confidences = [0.91,0.45,0.78,0.33,0.66]

x=0
for a in confidences:
    n=confidences[x]
    if n>=0.5:
        print(n)
    x=x+1

# batter alternative down below

for a in confidences:
    if a>=0.5:
        print(a)