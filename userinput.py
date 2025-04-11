from djitellopy import Tello
import keyboard
import time
from time import sleep
import cv2
import threading
def control_drone():
    
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")
    
    tello.takeoff()
    sleep(8)
    print("Drone has taken off!")

    try:
        while True:
            if keyboard.is_pressed("w"):
                tello.move_forward(30)
                print("Moved forward")
            elif keyboard.is_pressed("s"):
                tello.move_back(30)
                print("Moved backward")
            elif keyboard.is_pressed("a"):
                tello.move_left(30)
                print("Moved left")
            elif keyboard.is_pressed("d"):
                tello.move_right(30)
                print("Moved right")
            elif keyboard.is_pressed("up"):
                tello.move_up(30)
                print("Moved up")
            elif keyboard.is_pressed("down"):
                tello.move_down(30)
                print("Moved down")
            elif keyboard.is_pressed("left"):
                tello.rotate_counter_clockwise(30)
                print("Rotated left")
            elif keyboard.is_pressed("right"):
                tello.rotate_clockwise(30)
                print("Rotated right")
            elif keyboard.is_pressed("q"):
                print("Landing...")
                tello.land()
                break
            
            time.sleep(0.1)

    except Exception as e:
        print("Error:", e)
        tello.land()

def cam():
    while True:
        frame = tello.get_frame_read().frame
        cv2.imshow("Frame", frame)
        # While it is running, cv2 gets the current frame on the camera and outputs it to a window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

tello = Tello()
tello.streamon()
t1 = threading.Thread(target=cam, args=())
t2 = threading.Thread(target=control_drone, args=())
t1.start()
t2.start()
t1.join()
t2.join()
