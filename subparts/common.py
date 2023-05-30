import keyboard as kbd
import subparts.data as data
from pynput import mouse, keyboard

from enum import Enum, auto
import time

class Common:
    def __init__(self):
        self.mouse = mouse.Controller()
        self.kb = keyboard.Controller()
        self.data = data.Data(self)

    def check_break(self):
        return kbd.is_pressed("shift") or kbd.is_pressed("Esc")

    def click(self, coords):
            self.mouse.position = coords
            self.mouse.click(mouse.Button.left)
            self.wait_seconds(0.2)

    def scale_to_coords(self, coords):
        center = self.data.get_center()
        scale = self.data.get_scale()
        return (center[0]+(coords[0]*scale), center[1]+(coords[1]*scale))

    def click_from_center(self, scales):
        self.mouse.position = self.scale_to_coords(scales)
        self.mouse.click(mouse.Button.left)

    def hold_from_center(self, scales):
        self.mouse.position = self.scale_to_coords(scales)
        self.mouse.press(mouse.Button.left)

    def drag_from_center(self, start, end, time_to_wait = 0):
        """
        ToDo:
        Make use of pyautogui.drag()
        - Not useful
        """
        time_to_wait_between_actions = 0.1
        self.mouse.position = self.scale_to_coords(start)
        if self.check_break():
            return
        self.mouse.press(mouse.Button.left)
        self.wait_seconds(time_to_wait_between_actions)
        if self.check_break():
            return
        self.mouse.position = self.scale_to_coords(end)
        if self.check_break():
            self.mouse.release(mouse.Button.left)
            return
        self.wait_seconds(time_to_wait + time_to_wait_between_actions)
        self.mouse.release(mouse.Button.left)
        self.wait_seconds(time_to_wait_between_actions)

    def wait_seconds(self, seconds: float):
        time_start = time.time()
        while (time.time() - time_start < seconds):
            if self.check_break():
                break

    def write(self, text):
        self.kb.type(text)

    def key_press(self, button):
        self.kb.tap(button)

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
    TOP_LEFT = auto()
    BOTTOM_RIGHT = auto()
