import pyautogui
import keyboard
import time
import random

CODE = "FGJLMF"
def click():
    pyautogui.moveTo(330, 320)
    pyautogui.click(button='left')
    pyautogui.moveTo(680, 700)
    pyautogui.click(button='left')
    pyautogui.write(CODE)
    pyautogui.moveTo(860, 700)
    pyautogui.click(button='left')

def wait_seconds(seconds):
    print(f"Waiting {seconds} seconds.")
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if keyboard.is_pressed('z'):
            break
        continue
    pass

def cycle():
    running = True
    while True:
        try:
            if running:
                click()
                time_to_wait = 2
                wait_seconds(time_to_wait)
            if running and keyboard.is_pressed('z'):
                print("Pause")
                running = False
            if not running and keyboard.is_pressed('x'):
                print("Continue")
                running = True
        except KeyboardInterrupt:
            print("Ok, done!")
            break

if __name__ == '__main__':
    wait_seconds(5)
    cycle()

    