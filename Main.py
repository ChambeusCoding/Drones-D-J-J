from djitellopy import Tello
from time import sleep
tello = Tello()

tello.connect()
temp = tello.get_temperature()
# if int(temp) >= 50:
#     print("Temperature is too high, turning on motor for cooling")
#     tello.turn_motor_on()
#     sleep(50)
#     tello.turn_motor_off()
#     sleep(5)
tello.takeoff()
tello.move_back(100)
tello.rotate_clockwise(180)
tello.flip_back()
tello.flip_forward()
tello.flip_left()
tello.flip_right()
tello.move_forward(100)

tello.land()
