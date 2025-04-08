# from djitellopy import Tello
# import cv2
# import threading
# import time
# import logging

# # --- Enable detailed logging ---
# logging.basicConfig(level=logging.INFO)
# tello_logger = logging.getLogger('djitellopy')
# tello_logger.setLevel(logging.INFO)

# # --- Initialize Tello ---
# tello = Tello()

# try:
#     tello.connect()

#     tello.streamon()
#     time.sleep(2)  # Allow the video stream to stabilize
#     frame_read = tello.get_frame_read()
# except Exception as e:
#     print(f"[INIT ERROR] {e}")
#     exit(1)

# # --- Control flag for video thread ---
# keep_running = True

# # --- Video display thread ---
# def video_loop():
#     global keep_running
#     while keep_running:
#         frame = frame_read.frame
#         if frame is not None:
#             cv2.imshow("Tello Camera", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             keep_running = False
#             break
#     cv2.destroyAllWindows()

# # --- Flight control thread ---
# def flight_control():
#     try:
#         tello.takeoff()
#         time.sleep(1)

#         tello.move_up(100)
#         time.sleep(1)

#         tello.move_right(10)
#         time.sleep(1)

#         tello.move_left(10)
#         time.sleep(1)

#         tello.flip_forward()
#         time.sleep(1)

#         tello.flip_back()
#         time.sleep(1)

#         time.sleep(10)  # Hover for a bit
#         tello.land()
#     except Exception as e:
#         print(f"[FLIGHT ERROR] {e}")
#         tello.land()

# # --- Start threads ---
# video_thread = threading.Thread(target=video_loop)
# flight_thread = threading.Thread(target=flight_control)

# video_thread.start()
# flight_thread.start()

# # --- Wait for flight to complete ---
# flight_thread.join()

# # --- Stop video feed ---
# keep_running = False
# video_thread.join()

# # --- Cleanup ---
# tello.streamoff()
# print("Flight completed and video stopped.")

from djitellopy import Tello
import cv2
import threading
import time
import logging

# --- Enable logging ---
logging.basicConfig(level=logging.INFO)
tello_logger = logging.getLogger('djitellopy')
tello_logger.setLevel(logging.INFO)

# --- Initialize and connect to Tello ---
tello = Tello()

try:
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")
    
    tello.streamon()
    time.sleep(2)  # Let the stream initialize
    frame_read = tello.get_frame_read()

except Exception as e:
    print(f"[INIT ERROR] {e}")
    exit(1)

# --- Flag to control video thread ---
keep_running = True

# --- Video thread ---
def video_loop():
    global keep_running
    while keep_running:
        frame = frame_read.frame
        if frame is not None:
            cv2.imshow("Tello Camera", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            keep_running = False
            break
    cv2.destroyAllWindows()

# --- Flight control thread ---
def flight_control():
    
        tello.takeoff()
        time.sleep(1)

        tello.move_up(20)
        time.sleep(1)

        tello.move_right(20)
        time.sleep(1)

        tello.move_left(20)
        time.sleep(1)

        tello.flip_forward()
        time.sleep(1)

        tello.flip_back()
        time.sleep(1)

        print("[INFO] Hovering...")
        time.sleep(5)

        tello.land()

# --- Start threads ---
flight_thread = threading.Thread(target=flight_control)
video_thread = threading.Thread(target=video_loop)

flight_thread.start()
video_thread.start()

# --- Wait for flight to finish ---
flight_thread.join()

# --- Stop video after flight ---
keep_running = False
video_thread.join()

# --- Cleanup ---
tello.streamoff()
cv2.destroyAllWindows()
print("✅ Flight and video completed.")
