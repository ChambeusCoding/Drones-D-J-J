from djitellopy import Tello
from time import sleep
tello = Tello()

tello.connect()
temp = tello.get_temperature()
if int(temp) >= 50:
    print("Temperature is too high, turning on motor for cooling")
    tello.turn_motor_on()
    sleep(50)
    tello.turn_motor_off()
    sleep(5)
tello.takeoff()
tello.move_left(100)
for i in range(100):
    tello.rotate_counter_clockwise(90)
    i =+ 1
tello.move_forward(100)

tello.land()