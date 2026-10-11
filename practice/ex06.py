confidences = [0.91,0.45,0.78,0.33,0.66]

count=0
for a in confidences:
    if a>=0.5:
        count=count+1

print(count)