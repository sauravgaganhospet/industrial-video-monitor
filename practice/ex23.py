def video_length(frames,fps):
    dura=frames/fps
    return dura

print(f"The video is {video_length(900,30)} seconds long")