import numpy as np
import pyautogui 
import cv2
import datetime
import time

screen_size = pyautogui.size()
file_name = f"recording_{int(time.time())}.mp4"
fps = 60.0
codec = cv2.VideoWriter.fourcc(*"mp4v")
out = cv2.VideoWriter(file_name,codec,fps,screen_size)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live",480,270)

try:
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cv2.putText(frame,timestamp,(1,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        out.write(frame)
        cv2.imshow("Live",frame)

        if cv2.waitKey(1) == ord('q'):
            print("Recording Stopped.")
            break
    
except KeyboardInterrupt:
    print("Recording interrupted by user.")

out.release()
cv2.destroyAllWindows()