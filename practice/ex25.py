def crossed(prev_y, curr_y, line_y):
    if prev_y<line_y and curr_y>=line_y:
        return True
    else:
        return False

print(crossed(280,320,300))