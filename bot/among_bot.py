"""Auto-tasker"""

from ctypes import windll
import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import ttk

USE_BUTTON = (1260, 660)
ALIGN_CENTER = (884, 384)
ALIGN_PARABOLA_CONSTANT = 0.0008
RANGE_OF_ALIGN_UP_DOWN_VALUES = range(-277, 277, 20)


#####HELP######

def check_break():
    if keyboard.is_pressed('shift'):
        print("BREAK!")
    return keyboard.is_pressed('shift')

def wait_seconds(seconds):
    time_started = time.time()
    while time.time() - time_started < seconds:
        if check_break():
            break

def wait_for_cross(cross):
    while check_cross(cross):
        if check_break():
            break

def check_cross(coords):
    return check_coords(coords[0], coords[1]) == (238, 238, 238)

def drag_from(coords_1, coords_2, waiting_time=0):
    """
    ToDo:
    Make use of pyautogui.drag()
    - Not useful
    """
    
    pyautogui.moveTo(coords_1)
    if check_break():
        return
    pyautogui.mouseDown()
    if check_break():
        return
    pyautogui.moveTo(coords_2)
    if check_break():
        pyautogui.mouseUp()
        return
    wait_seconds(waiting_time)
    pyautogui.mouseUp()

def drag_slowly(coords_1, coords_2, time):
    x_diff = (coords_2[0] - coords_1[0])
    y_diff = (coords_2[1] - coords_1[1])
    pyautogui.mouseDown()
    pyautogui.moveTo(coords_1)
    pyautogui.move(x_diff, y_diff, time)
    pyautogui.mouseUp()

def get_wire_color(x, y):
    r, g, b = check_coords(x, y)
    if r > 250 and g < 10 and b < 1:
        return "red"
    elif r < 40 and g < 40 and b == 255:
        return "blue"
    elif r > 250 and g > 200 and b < 10:
        return "yellow"
    elif r > 250 and b > 250 and g < 10:
        return "purple"
    return "yo wtf"

def check_coords(x=None, y=None):
    hdc = windll.user32.GetDC(0)
    pixel = windll.gdi32.GetPixel(hdc, x, y)
    #pixel = windll.gdi32.GetPixel(hdc, 684, 560)
    i_colour = int(pixel)
    r = (i_colour & 0xff)
    g = ((i_colour >> 8) & 0xff)
    b = ((i_colour >> 16) & 0xff)
    return (r, g, b)

def check_simon_lights():
    lights = [(340 + i*60, 225) for i in range(5)]
    count = 0
    while count < 1:
        if check_break():
            break
        for i, light in enumerate(lights):
            if check_coords(light[0], light[1])[1] > 150:
                print(f"{i}: on")
                count += 1
            else:
                print(f"{i}: off")
    return count

def get_square_value(coords):
    if check_coords(coords[0] + 12, coords[1] + 41)[0] < 70:
        return 1
    if check_coords(coords[0] + 13, coords[1] + 35)[0] < 70:
        return 2
    if check_coords(coords[0] + 19, coords[1] + 40)[0] < 70:
        return 4
    if check_coords(coords[0] + 7, coords[1] + 20)[0] < 70:
        return 5
    if check_coords(coords[0] + 26, coords[1] + 24)[0] < 70:
        return 6
    if check_coords(coords[0] + 15, coords[1] + 36)[0] < 70:
        return 7
    if check_coords(coords[0] + 23, coords[1] + 26)[0] < 70:
        return 8
    if check_coords(coords[0] + 26, coords[1] + 15)[0] < 70:
        return 9
    if check_coords(coords[0] + 10, coords[1] + 13)[0] < 70:
        return 10
    return 3

#####CYCLE#####

def move():
    raise NotImplementedError


def start_task():
    pyautogui.click(10, 10)
    pyautogui.click(USE_BUTTON)
    wait_seconds(1)


def do_task(task_to_do):
    print(f"Doing {task_to_do}.")
    tasks = {
        "align": lambda: align(),
        "asteroids": lambda: asteroids(),
        "calibrate distributor": lambda: calibrate_distributor(),
        "card": lambda: card(),
        "course": lambda: course(),
        "divert-1": lambda: divert_1(),
        "divert-2": lambda: center_click(),
        "download-upload": lambda: download_upload(),
        "fuel": lambda: fuel(),
        "leaves": lambda: leaves(),
        "manifolds": lambda: manifolds(),
        "sample": lambda: sample(),
        "scan": lambda: scan(),
        "shields": lambda: shields(),
        "simon says": lambda: simon_says(),
        "stabilize": lambda: center_click(),
        "trash": lambda: trash(),
        "vent": lambda: vent(),
        "wires": lambda: wires()
    }
    start_task()
    tasks[task_to_do]()
    print("Done!")
    wait_seconds(2)

#####TASKS#####


def align():
    for x in RANGE_OF_ALIGN_UP_DOWN_VALUES:
        y = int(ALIGN_PARABOLA_CONSTANT * x ** 2)
        actual_coords = (ALIGN_CENTER[0] + y, ALIGN_CENTER[1] + x)
        r, g, b = check_coords(actual_coords[0], actual_coords[1])
        if max(r, g, b) > 70:
            drag_from(actual_coords, ALIGN_CENTER)
            break
        if check_break():
            break

def asteroids():
    cross = (340, 92)
    origin = (500, 200)
    size = 396
    step = 10
    while check_cross(cross):
        for y in range(0, size+1, step):
            coord_x, coord_y = origin[0]+size, origin[1]+y
            if check_break():
                return
            # pyautogui.moveTo(coord_x, coord_y)
            pyautogui.click(coord_x, coord_y)

def calibrate_distributor():
    while check_coords(875, 170) == (0, 0, 0):
        if check_break():
            return
        continue
    pyautogui.click(875, 220)
    while check_coords(875, 350) == (0, 0, 0):
        if check_break():
            return
        continue
    pyautogui.click(875, 420)
    while check_coords(875, 540) == (0, 0, 0):
        if check_break():
            return
        continue
    pyautogui.click(875, 600)

def card():
    pyautogui.click(580, 580)
    wait_seconds(1)

    if check_break():
            return
    drag_slowly((370, 300), (1030, 300), 1.05)
    pyautogui.mouseUp()

def center_click():
    pyautogui.click(683, 383)

def course():
    raise NotImplementedError

def divert_1():
    switches_x = [443, 510, 578, 648, 717, 784, 854, 923]
    switches_y = 560

    for x in switches_x:
        if check_coords(x, switches_y)[0] > 100:
            drag_from((x, switches_y), (x, 400))

def download_upload():
    cross = (238, 169)
    pyautogui.click(680, 470)
    wait_for_cross(cross)

def fuel():
    pyautogui.moveTo(1040, 620)
    pyautogui.mouseDown()
    wait_seconds(4)
    pyautogui.mouseUp()

def leaves():
    false = [(140,166,214), (207, 233, 247)]
    positive = [(198,146,66), (71, 77, 19)]
    steps = 50
    field_x = range(496, 996, steps)
    field_y = range(70, 697, steps)
    cross = (340, 110)
    finish = (380, 380)
    
    while check_cross(cross):
        if check_break():
            break
        for x in field_x:
            if check_break() or not check_cross(cross):
                break
            for y in field_y:
                if check_break() or not check_cross(cross):
                    break
                if check_coords(x, y)[2] < 150:
                    drag_from((x, y), finish)
                    
    print("Finished leaves!")

def manifolds():
    x_diff = 109
    y_diff = 111
    squares = []
    for y in range(2):
        y_coord = 304 + y*y_diff
        for x in range(5):
            x_coord = 447 + x*x_diff
            squares.append(get_square_value((x_coord, y_coord)))
    print(squares)
    for i in range(1, 11):
        square_to_press = squares.index(i)
        pyautogui.click(447+(square_to_press %5)*x_diff, 304+(square_to_press // 5)*y_diff)

def sample():
    pyautogui.click(900, 670)
    wait_seconds(62)
    for i in range(5):
        x = 520 + 80 * i
        button_y = 600
        liquid_y = 420
        print(check_coords(x, liquid_y))
        if check_coords(x, liquid_y) == (246, 134, 134):
            pyautogui.click(x, button_y)
            break

def scan():
    cross = (340, 110)
    wait_for_cross(cross)

def shields():
    coords = [
        (682, 288),  # 241, 21, 25
        (602, 329),  # 242, 21, 26
        (602, 450),  # 241, 22, 27
        (671, 482),  # 240, 22, 27
        (762, 450),  # 236, 30, 37
        (758, 319),  # 244, 17, 20
        (740, 318)  # 241, 21, 26
    ]
    for coord in coords:
        g = check_coords(coord[0], coord[1])[1]
        if g < 50:
            pyautogui.click(coord)

def simon_says():
    lights = []
    buttons = []
    for row in range(340, 521, 90):
        for column in range(370, 551, 90):
            lights.append((column, row))
        for column in range(810, 991, 90):
            buttons.append((column, row))
    i = check_simon_lights()
    while i < 6:
        print(i)
        order_to_press = []
        while len(order_to_press) < i:
            for j, light in enumerate(lights):
                if check_break():
                    return
                if check_coords(light[0], light[1]) != (0, 0, 0):
                    order_to_press.append(buttons[j])
                    wait_seconds(0.2)
        print([buttons.index(element) for element in order_to_press])
        wait_seconds(0.5)
        for button in order_to_press:
            if check_break():
                    return
            pyautogui.click(button)
            if check_coords(button[0], button[1]) == (189, 43, 0):
                i = 0
        i += 1

def trash():
    drag_from((900, 300), (900, 500), 2)

def vent():
    center_click()
    cross = (340, 90)
    origin = (383, 116)
    size = (600, 530)
    step = 50
    for x in range(origin[0], origin[0] + size[0] + 1, step):
        for y in range(origin[1], origin[1] + size[1] + 1, step):
            if check_cross(cross) and not check_break():
                pyautogui.click(x, y)
            else:
                return

def wires():
    x = [400, 940]
    y = [193, 326, 458, 590]
    for i in range(4):
        wire_color = check_coords(x[0], y[i])
        for j in range(4):
            other_wire = check_coords(x[1], y[j])
            if wire_color == other_wire:
                drag_from((x[0], y[i]), (x[1], y[j]))
                break

#####MAIN######

if __name__ == '__main__':
    list_of_tasks = [
        "align",
        "asteroids",
        "calibrate distributor",
        "card",
        "course",
        "divert-1",
        "divert-2",
        "download-upload",
        "fuel",
        "leaves",
        "manifolds",
        "sample",
        "scan",
        "shields",
        "simon says",
        "stabilize",
        "trash",
        "vent",
        "wires"
    ]
    root = tk.Tk()
    root.title("Tasker")
    root.columnconfigure(0, weight=1, uniform="A")
    root.columnconfigure(1, weight=1, uniform="A")
    root.columnconfigure(2, weight=1, uniform="A")
    root.columnconfigure(3, weight=1, uniform="A")
    for i, task in enumerate(list_of_tasks):
        ttk.Button(root, text=task, command = lambda task=task: do_task(task)).grid(row = i//4, column=i%4, sticky="NEWS")
    root.mainloop()
    # cycle()
