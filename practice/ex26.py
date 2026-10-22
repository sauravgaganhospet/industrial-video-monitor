
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

line_y = 300
crossed_ids = set()
prev = frames[0]

for frame_number, curr in enumerate(frames[1:], start=2):
    for bottle_id in curr:
        if bottle_id in prev and bottle_id not in crossed_ids:
            if crossed(prev[bottle_id], curr[bottle_id], line_y):
                crossed_ids.add(bottle_id)
                print(f"ID {bottle_id} crossed in frame {frame_number}")

    prev = curr

print("Crossed IDs:", crossed_ids)
print("Total:", len(crossed_ids))
