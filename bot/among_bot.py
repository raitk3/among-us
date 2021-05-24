"""Auto-tasker"""

from ctypes import windll
import pyautogui
import time


USE_BUTTON = (1260, 660)
ALIGN_CENTER = (884, 384)
ALIGN_PARABOLA_CONSTANT = 0.0008
RANGE_OF_ALIGN_UP_DOWN_VALUES = range(-277, 277, 20)


#####HELP######
def drag_from(coords_1, coords_2, waiting_time=0):
    """
    ToDo:
    Make use of pyautogui.drag()
    """
    pyautogui.moveTo(coords_1)
    pyautogui.mouseDown()
    pyautogui.moveTo(coords_2)
    time.sleep(waiting_time)
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


#####CYCLE#####

def move():
    raise NotImplementedError


def start_task():
    pyautogui.click(USE_BUTTON)
    time.sleep(1)


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
        "manifolds": lambda: manifolds(),
        "sample": lambda: sample(),
        "scan": lambda: scan(),
        "shields": lambda: shields(),
        "simon says": lambda: simon_says(),
        "stabilize": lambda: center_click(),
        "trash": lambda: trash(),
        "wires": lambda: wires()
    }
    start_task()
    tasks[task_to_do]()
    print("Done!")
    time.sleep(2)

#####TASKS#####


def align():
    for x in RANGE_OF_ALIGN_UP_DOWN_VALUES:
        y = int(ALIGN_PARABOLA_CONSTANT * x ** 2)
        actual_coords = (ALIGN_CENTER[0] + y, ALIGN_CENTER[1] + x)
        r, g, b = check_coords(actual_coords[0], actual_coords[1])
        if max(r, g, b) > 70:
            drag_from(actual_coords, ALIGN_CENTER)
            break


def asteroids():
    raise NotImplementedError


def calibrate_distributor():
    while check_coords(875, 170) == (0, 0, 0):
        continue
    pyautogui.click(875, 220)
    while check_coords(875, 350) == (0, 0, 0):
        continue
    pyautogui.click(875, 420)
    while check_coords(875, 540) == (0, 0, 0):
        continue
    pyautogui.click(875, 600)


def card():
    pyautogui.click(580, 580)
    time.sleep(1)
    pyautogui.moveTo(370, 300)
    pyautogui.mouseDown()
    pyautogui.drag(700, 0, 1, button='left')
    pyautogui.mouseUp()


def center_click():
    pyautogui.click(683, 383)


def course():
    raise NotImplementedError


def divert_1():
    switches_x = [443, 510, 578, 648, 717, 784, 854, 923]
    switches_y = 560

    for i, x in enumerate(switches_x):
        r, g, b = check_coords(x, switches_y)
        if r > 100:
            drag_from((x, switches_y), (x, 400))


def download_upload():
    pyautogui.click(680, 470)
    time.sleep(10)


def fuel():
    pyautogui.moveTo(1040, 620)
    pyautogui.mouseDown()
    time.sleep(4)
    pyautogui.mouseUp()


def manifolds():
    raise NotImplementedError


def sample():
    pyautogui.click(900, 670)
    time.sleep(62)
    for i in range(5):
        x = 520 + 80 * i
        button_y = 600
        liquid_y = 420
        print(check_coords(x, liquid_y))
        if check_coords(x, liquid_y) == (246, 134, 134):
            pyautogui.click(x, button_y)
            break


def scan():
    time.sleep(10)


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
    i = 1
    while i < 6:
        print(i)
        order_to_press = []
        while len(order_to_press) < i:
            for j, light in enumerate(lights):
                if check_coords(light[0], light[1]) != (0, 0, 0):
                    order_to_press.append(buttons[j])
                    time.sleep(0.2)
            print([buttons.index(element) for element in order_to_press])
        time.sleep(0.5)
        for button in order_to_press:
            pyautogui.click(button)
            if check_coords(button[0], button[1]) == (189, 43, 0):
                i = 0
        i += 1


def trash():
    drag_from((900, 300), (900, 500), 2)


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

# if __name__ == '__main__':
    # do_task("align")
    # cycle()
