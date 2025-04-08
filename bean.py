from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()
tello.takeoff()
tello.move_forward(10)
tello.move_left(10)
tello.move_back(10)
tello.move_right(10)
tello.flip_forward()
tello.land()
tello.streamoff()
tello.end()