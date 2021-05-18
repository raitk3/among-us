import pyautogui
import keyboard
import time
import random

CODE = "DIJTMF"
CROSS = (330, 320)
TEXTBOX = (680, 700)
ARROW = (860, 700)


def click():

    pyautogui.click(CROSS)
    time.sleep(0.1)
    pyautogui.click(TEXTBOX)
    time.sleep(0.1)
    pyautogui.write(CODE)
    pyautogui.click(ARROW)


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
