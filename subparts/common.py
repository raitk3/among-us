import keyboard as kbd
from pynput import keyboard
import numpy as np

from enum import Enum, auto
import time

def check_break(kb=None):
    if kb == None:
        kb = keyboard.Controller()
    return kbd.is_pressed("shift") or kbd.is_pressed("Esc")

def wait_seconds(seconds: float, kb=None):
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if check_break(kb):
            break

def write(text, kb=None):
    kb = kb if kb != None else keyboard.Controller()
    kb.type(text)

def key_press(button, kb=None):
    kb = kb if kb != None else keyboard.Controller()
    kb.tap(button)


def cart_to_polar(center, x, y):
    diff_x, diff_y = center[0] - x, center[1] - y
    rho = np.sqrt(diff_x**2 + diff_y**2)
    phi = np.arctan2(diff_y, diff_x)
    return rho, phi

def polar_to_cart(center, rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return center[0] + x, center[1] + y

class State(Enum):
    MENU = auto()
    JOIN = auto()
    SENTENCES = auto()
    SETTINGS = auto()
    TASKS = auto()
    ABOUT = auto()


class Coordinate(Enum):
    CROSS = auto()
    TB_1 = auto()
    TB_2 = auto()
    ARROW = auto()
    ORIGIN = auto()
    DISPLAY = auto()
