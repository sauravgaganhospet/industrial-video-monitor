positions = {1: 120, 2: 340, 3: 95}     # bottle ID -> its y position

print(positions[2])         # look up ID 2 -> 340
positions[1] = 150          # update ID 1
positions[4] = 200          # add a new ID
print(len(positions))       # how many entries: 4

if 5 in positions:          # check whether a key exists
    print("seen before")

print(positions.get(5))     # .get() returns None instead of crashing if missing

for bottle_id, y in positions.items():   # loop over keys and values together
    print(f"ID {bottle_id} is at y={y}")