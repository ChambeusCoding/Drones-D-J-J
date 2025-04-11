from djitellopy import Tello
import cv2
import threading
from time import sleep

def move():
    tello.rotate_clockwise(135)
    sleep(12)
    tello.flip_forward()
    tello.set_speed(100)
    tello.move_up(80)
    tello.move_back(200)
    tello.move_forward(200)
    tello.rotate_counter_clockwise(360)
    tello.rotate_clockwise(360)
    # tello.move_up(40)
    # tello.move_forward(20)
    # tello.move_left(20)
    # tello.move_back(20)
    # tello.move_right(20)
    # tello.flip_forward()

def cam():
    while True:
        frame = tello.get_frame_read().frame
        cv2.imshow("Frame", frame)
        # While it is running, cv2 gets the current frame on the camera and outputs it to a window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

tello = Tello()
tello.connect()
tello.streamon()
tello.takeoff()
t1 = threading.Thread(target=cam, args=())
t2 = threading.Thread(target=move, args=())
t1.start()
t2.start()
t1.join()
t2.join()
tello.land()
tello.streamoff()
tello.end()