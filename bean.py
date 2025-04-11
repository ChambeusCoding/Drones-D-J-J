from djitellopy import Tello
import cv2
import threading
from time import sleep
import os
import pygame

def play_boss_music():
    try:
        pygame.mixer.init()
        music_path = os.path.abspath("spin.mp3")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(loops=-1)
        
    except Exception as e:
        print("Error with playing sound.")
        print(e)

def move():
    tello.move_up(30)
    play_boss_music()
    for i in range(25):
        tello.rotate_clockwise(360)
        i += 1
        print(i)

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