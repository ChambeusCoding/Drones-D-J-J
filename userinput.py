from djitellopy import Tello
import keyboard
import time
from time import sleep
from datetime import datetime
import cv2
import threading
import numpy as np
import pygame
import os

# def get_data():
#     # tello.query_sdk_version()
#     # tello.query_serial_number()
#     while True:
#         try:
#             tello.get_barometer()
#             tello.get_height()
#             tello.get_battery()
#             tello.get_flight_time()
#             tello.get_pitch()
#             tello.get_roll()
#             tello.get_temperature()
#             tello.get_yaw()
#         except KeyboardInterrupt:
#             break
def playMusic():
    try:
        pygame.mixer.init()
        music_path = os.path.abspath("spin.mp3")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(loops=-1)
        
    except Exception as e:
        print("Error with playing sound.")
        print(e)
def victory():
    playMusic()
    for i in range(10):
        tello.rotate_clockwise(360)
        i += 1
def control_drone():
    print(f"Battery: {tello.get_battery()}%")
    
    tello.takeoff()
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
                tello.end()
                break
            elif keyboard.is_pressed("l"):
                print("Emergency stop happening in 5 seconds. Be ready to catch.")
                sleep(5)
                tello.emergency()
                tello.end()
                break
            elif keyboard.is_pressed("e"):
                print("Flipped forward.")
                tello.flip_forward()
            elif keyboard.is_pressed("f"):
                print("Flipped backwards.")
                tello.flip_back()
            elif keyboard.is_pressed("r"):
                tello.flip_left()
                print("Flipped left.")
            elif keyboard.is_pressed("t"):
                tello.flip_right()
                print("Flipped right.")
            # elif keyboard.is_pressed("i"):
            #     get_data()
            elif keyboard.is_pressed("v"):
                print("Victory dance.")
                victory()
                tello.land()
                tello.end()
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

# def colordetect():
#     tello.streamon()
#     print("Starting color detection...")

#     # Ensure 'test runs' folder exists
#     folder_name = "test runs"
#     os.makedirs(folder_name, exist_ok=True)

#     # Create timestamped file inside the folder
#     timestamp = datetime.now().strftime("%d-%m-%Y-%I:%M:%S %p")
#     filename = "RUNS.txt"

#     with open(filename, 'w') as file:
#         while True:
#             frame = tello.get_frame_read().frame
#             hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#             # Define HSV color ranges
#             color_ranges = {
#                 "Red": [(0, 120, 70), (10, 255, 255)],
#                 "Orange": [(11, 100, 100), (25, 255, 255)],
#                 "Yellow": [(26, 100, 100), (34, 255, 255)],
#                 "Green": [(35, 100, 100), (85, 255, 255)],
#                 "Blue": [(86, 100, 100), (125, 255, 255)],
#                 "Purple": [(126, 100, 100), (160, 255, 255)],
#             }

#             largest_area = 0
#             closest_color = None

#             for color, (lower, upper) in color_ranges.items():
#                 mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
#                 contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#                 for cnt in contours:
#                     area = cv2.contourArea(cnt)
#                     if area > largest_area:
#                         largest_area = area
#                         closest_color = color

#             # Log the closest color
#             if closest_color:
#                 log = f"[{datetime.now().strftime('%I:%M:%S %p')}] Closest Color: {closest_color}"
#                 print(log)
#                 file.write(log + "\n")
#                 file.flush()

#             # Wait 5 seconds before next detection
#             time.sleep(5)

#             # Optional break with key press
#             if keyboard.is_pressed("i"):
#                 break

#     cv2.destroyAllWindows()
#     print(f"Detection session saved to '{filename}'")

def colordetect():
    tello.streamon()
    print("Color detection armed. Press SPACEBAR to scan.")

    filename = "RUNS.txt"

    if not os.path.exists(filename):
        open(filename, 'w').close()

    with open(filename, 'a') as file:
        while True:
            frame = tello.get_frame_read().frame
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            cv2.imshow("Tello Camera", frame)

            if keyboard.is_pressed("space"):
                print("[SPACEBAR] Scan triggered.")
                color_ranges = {
                "Red": [  # Red wraps around hue = 0, so we need two ranges
                    (np.array([0, 150, 120]), np.array([10, 255, 255])),
                    (np.array([170, 150, 120]), np.array([180, 255, 255]))
                ],
                "Orange": [
                    (np.array([11, 180, 150]), np.array([20, 255, 255]))
                ],
                "Yellow": [
                    (np.array([21, 180, 150]), np.array([30, 255, 255]))
                ],
                "Green": [
                    (np.array([36, 150, 120]), np.array([80, 255, 255]))
                ],
                "Blue": [
                    (np.array([95, 150, 120]), np.array([125, 255, 255]))
                ],
                "Purple": [
                    (np.array([130, 170, 150]), np.array([155, 255, 255]))
                ],
            }
                largest_area = 0
                closest_color = None

                for color, ranges in color_ranges.items():
                    if not isinstance(ranges[0], tuple):
                        ranges = [ranges]  # ensure all are lists of tuples
                    mask = None
                    for lower, upper in ranges:
                        this_mask = cv2.inRange(hsv, lower, upper)
                        mask = this_mask if mask is None else cv2.bitwise_or(mask, this_mask)
                    
                    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    
                    for cnt in contours:
                        area = cv2.contourArea(cnt)
                        if area > largest_area:
                            largest_area = area
                            closest_color = color
                    for cnt in contours:
                        area = cv2.contourArea(cnt)
                        if area > largest_area:
                            largest_area = area
                            closest_color = color
                if closest_color:
                    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                    log = f"[{timestamp}] Closest Color: {closest_color}"
                    print(log)  # Echo to terminal
                    file.write(log + "\n")
                    file.flush()
                else:
                    print("No dominant color detected.")

                while keyboard.is_pressed("space"):
                    pass

            if cv2.waitKey(1) == 27:  # ESC only affects camera window
                break

    cv2.destroyAllWindows()

tello = Tello()
tello.connect()
tello.streamon()
t1 = threading.Thread(target=cam, args=())
t2 = threading.Thread(target=control_drone, args=())
t3 = threading.Thread(target=colordetect, args=()) 
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
# t3.join()
