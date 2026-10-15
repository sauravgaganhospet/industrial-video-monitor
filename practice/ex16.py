positions= {1:120,2:340,3:95}

print(f"the y of ID 2={positions[2]}\n")

positions[1]=150
positions[4]=200

for A_id, y in positions.items():
    print(f"For ID {A_id} the value is {y}.\n")