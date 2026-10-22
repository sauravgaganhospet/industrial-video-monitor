import cv2

def video_length(frames, fps):
    return frames/fps

cap = cv2.VideoCapture("data/line1.mp4")

if not cap.isOpened():
    print("Error: could not open the video!")
    exit()

fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

length = video_length(frame_count,fps)

print(f"FPS: {fps}")
print(f"Size: {width} x {height}")
print(f"Frames: {frame_count}")
print(f"Length: {length:.1f} seconds")

cap.release()