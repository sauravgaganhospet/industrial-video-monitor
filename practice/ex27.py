def crossed(prev_y, curr_y, line_y):
    if prev_y < line_y and curr_y >= line_y:
        return True
    else:
        return False


frames = [
    {1: 270, 2: 290},
    {1: 295, 2: 305},
    {1: 310, 2: 320},
    {1: 320, 2: 330, 3: 100},
]

line_y=300
crossed_id=set()
prev=frames[0]

for curr in frames[1:]:
    for bottle_id in curr:
        if bottle_id in prev:
            if crossed(prev[bottle_id],curr[bottle_id],line_y):
                crossed_id.add(bottle_id)
prev=curr

print(crossed_id)
print(len(crossed_id))