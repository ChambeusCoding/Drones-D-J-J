from djitellopy import Tello
import cv2
import time

tello = Tello()

try:
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")
    
    tello.streamon()
    time.sleep(2)
    
    frame_read = tello.get_frame_read()

    while True:
        frame = frame_read.frame
        if frame is not None:
            cv2.imshow("Tello", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print("ERROR:", e)

finally:
    tello.streamoff()
    cv2.destroyAllWindows()
