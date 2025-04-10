from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_up(65)
sleep(1)
tello.move_up(50)
tello.move_right(20)
tello.move_forward(215)
sleep(1)
tello.move_forward(215)
tello.move_right(20)
tello.move_down(50)
tello.rotate_counter_clockwise(90)
tello.move_forward(90)
tello.move_back(110)
tello.rotate_clockwise(90)
tello.move_up(70)
tello.move_forward(152)
tello.rotate_counter_clockwise(90)
tello.move_forward(40)
tello.rotate_clockwise(90)
tello.move_forward(60)
tello.move_right(70)
tello.move_forward(50)
tello.move_right(80)
tello.move_forward(50)
tello.move_down(50)
tello.rotate_counter_clockwise(45)
tello.move_forward(50)
tello.land()
tello.end()