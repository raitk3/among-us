import keyboard as kbd
import time
from PIL import ImageGrab
from pynput import mouse

def wait_seconds(seconds: float):
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if check_break():
            break

def click(m, coords):
    m.position = coords
    m.click(mouse.Button.left)
    wait_seconds(0.2)

def check_break():
    return kbd.is_pressed("shift") or kbd.is_pressed("Esc")

def get_screenshot():
    image = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    pixels = image.load()
    return pixels

def start_game(m):
    print("Start game")
    click(m, (900, 800))

def end1(m):
    print("Finished")
    click(m, (1560, 900))

def end2(m):
    print("Open lobby again")
    click(m, (1850, 900))

def main():
    m = mouse.Controller()
    while not check_break():
        screenshot = get_screenshot()
        red = (220, 49, 22)
        grey = (170, 179, 184)
        black = (0, 0, 0)
        green = (0, 255, 0)
        white = (255, 255, 255)
        if screenshot[1175, 949] == green:
            wait_seconds(2)
            start_game(m)
            wait_seconds(10)
        if screenshot[1385, 900] == black and \
           screenshot[1392, 900] == white:
            end1(m)
        if screenshot[800, 950] == red and \
           screenshot[1850, 880] == grey:
            end2(m)
        wait_seconds(1)
    

if __name__ == '__main__':
    main()