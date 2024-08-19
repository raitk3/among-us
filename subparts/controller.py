import pygame
from enum import Enum

class Button(Enum):
    A = 0
    B = 1
    X = 2
    Y = 3
    L1 = 4
    L2 = 5
    SHARE = 6
    START = 7
    L_JOY = 8
    R_JOY = 9
    SCREEN = 10

class Controller():
    def __init__(self, program) -> None:
        self.program = program
        self.enabled = False
        self.connect_device()

    def connect_device(self):
        try:
            pygame.joystick.init()
            self.controller = pygame.joystick.Joystick(0)
            self.combos = {}
            self.enabled = True
        except pygame.error:
            self.enabled = False


    def check_combos(self):
        if not self.enabled:
            self.connect_device()

        if self.enabled:
            try:
                if self.controller.get_button(Button.L_JOY.value) and self.controller.get_button(Button.R_JOY.value):
                    if not self.combos["card"]:
                        self.program.tasks.start_task()
                        self.program.tasks.card()
                    self.combos["card"] = True
                else:
                    self.combos["card"] = False

                if self.controller.get_button(Button.L_JOY.value) and self.controller.get_button(Button.B.value):
                    if not self.combos["wires"]:
                        self.program.tasks.start_task()
                        self.program.tasks.wires()
                    self.combos["wires"] = True
                else:
                    self.combos["wires"] = False

                if self.controller.get_button(Button.L_JOY.value) and self.controller.get_button(Button.X.value):
                    if not self.combos["covid"]:
                        self.program.tasks.toggle_kill()
                    self.combos["covid"] = True
                else:
                    self.combos["covid"] = False
            except pygame.error:
                self.enabled = False