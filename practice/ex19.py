prev = {1: 280, 2: 310, 3: 250}            # positions last frame
curr = {1: 305, 2: 320, 3: 260, 4: 100}    # positions this frame
line_y= 300

for bottle_id in curr:
    if bottle_id in prev:
        if curr[bottle_id]>=line_y and prev[bottle_id]<line_y:
            print(f"ID {bottle_id} passed.")
        else:
            print(f"ID {bottle_id} not passed")