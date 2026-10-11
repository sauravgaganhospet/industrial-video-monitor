confidence = 0.42
if confidence >= 0.5:
    print("keep this detection")
elif confidence >= 0.3:
    print("Uncertain")
else:
    print("Discard")