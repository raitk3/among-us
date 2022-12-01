from ast import Pass
from subparts.common import *
from pynput import mouse
class Tasks:
    def __init__(self, program):
        self.use_button = (0, 0)
        self.program = program
        self.mouse = self.program.mouse
        self.keyboard = self.program.keyboard
        self.mouse = self.program.mouse
        self.kill_status = False
        self.tasks = {
            # command, enabled, usebutton
            "Align": (lambda: self.align(), False, True),
            "Asteroids": (lambda: self.asteroids(), False, True),
            "Calibrate distributor": (lambda: self.calibrate_distributor(), False, True),
            "Chart course": (lambda: self.course(), False, True),
            "Clean vent": (lambda: self.vent(), False, True),
            "Divert 1": (lambda: self.divert_1(), False, True),
            "Divert 2": (lambda: self.center_click(), True, True),
            "Download/Upload": (lambda: self.download_upload(), False, True),
            "Fix wiring": (lambda: self.wires(), False, True),
            "Fuel engines": (lambda: self.fuel(), False, True),
            "Inspect sample": (lambda: self.sample(), False, True),
            "Leaves": (lambda: self.leaves(), False, True),
            "Scan": (lambda: self.scan(), False, True),
            "Shields": (lambda: self.shields(), False, True),
            "Stabilize steering": (lambda: self.center_click(), True, True),
            "Start reactor": (lambda: self.simon_says(), False, True),
            "Swipe card": (lambda: self.card(), False, True),
            "Trash": (lambda: self.trash(), False, True),
            "Unlock manifolds": (lambda: self.manifolds(), False, True),
            "COVID": (lambda: self.kill(), True, False)
        }

    #####HELP######

    def get_screenshot(self):
        return self.program.data.get_screenshot()

    def click(self, coords):
        self.program.data.click(coords, self.mouse)

    def check_cross(self, coords, image=None):
        if image == None:
            image = self.get_screenshot()
        return image[(coords[0], coords[1])] == (238, 238, 238)

    def wait_for_cross(self, cross):
        while self.check_cross(cross):
            if check_break():
                break

    def drag_from(self, coords_1, coords_2, waiting_time=0):
        """
        ToDo:
        Make use of pyautogui.drag()
        - Not useful
        """
        time_to_wait_between_actions = 0.1
        self.mouse.position = self.program.data.correct_coords(coords_1)
        if check_break(self.keyboard):
            return
        self.mouse.press(mouse.Button.left)
        wait_seconds(time_to_wait_between_actions)
        if check_break(self.keyboard):
            return
        self.mouse.position = self.program.data.correct_coords(coords_2)
        if check_break(self.keyboard):
            self.mouse.release(mouse.Button.left)
            return
        wait_seconds(waiting_time + time_to_wait_between_actions)
        self.mouse.release(mouse.Button.left)
        wait_seconds(time_to_wait_between_actions)

    def drag_slowly(self, coords_1, coords_2, steps):
        x_diff = (coords_2[0] - coords_1[0])
        y_diff = (coords_2[1] - coords_1[1])
        self.mouse.position = self.program.data.correct_coords(coords_1)
        self.mouse.press(mouse.Button.left)
        for _ in range(steps):
            self.mouse.move(x_diff//steps, y_diff//steps)
            wait_seconds(0.5 / steps)
        self.mouse.release(mouse.Button.left)

    def get_wire_color(self, x, y, picture=None):
        if picture == None:
            picture = self.get_screenshot()
        r, g, b = self.check_coords(x, y)
        if r > 250 and g < 10 and b < 1:
            return "red"
        elif r < 40 and g < 40 and b == 255:
            return "blue"
        elif r > 250 and g > 200 and b < 10:
            return "yellow"
        elif r > 250 and b > 250 and g < 10:
            return "purple"
        return "yo wtf"

    def check_simon_lights(self):
        lights = [(340 + i*60, 225) for i in range(5)]
        count = 0

        while count < 1:
            if check_break():
                break
            image = self.get_screenshot()
            for i, light in enumerate(lights):
                if image[(light[0], light[1])][1] > 150:
                    # print(f"{i}: on")
                    count += 1
                else:
                    pass
                    # print(f"{i}: off")
        return count

    def get_square_value(self, coords, image=None):
        if image == None:
            image = self.get_screenshot()
        if image[(coords[0] + 12, coords[1] + 41)][0] < 70:
            return 1
        if image[(coords[0] + 13, coords[1] + 35)][0] < 70:
            return 2
        if image[(coords[0] + 19, coords[1] + 40)][0] < 70:
            return 4
        if image[(coords[0] + 7, coords[1] + 20)][0] < 70:
            return 5
        if image[(coords[0] + 26, coords[1] + 24)][0] < 70:
            return 6
        if image[(coords[0] + 15, coords[1] + 36)][0] < 70:
            return 7
        if image[(coords[0] + 23, coords[1] + 26)][0] < 70:
            return 8
        if image[(coords[0] + 26, coords[1] + 15)][0] < 70:
            return 9
        if image[(coords[0] + 10, coords[1] + 13)][0] < 70:
            return 10
        return 3

    def toggle_kill(self):
        self.kill_status = not self.kill_status

    #####CYCLE#####

    def start_task(self):
        self.click((10, 10))
        self.click(self.use_button)
        wait_seconds(0.5)

    def do_task(self, task_to_do):
        task = self.tasks[task_to_do]
        if task[2]:
            self.start_task()
        task[0]()
        if task[2]:
            wait_seconds(2)

    #####TASKS#####

    def align(self):
        pass
           
    def asteroids(self):
        pass
           
    def calibrate_distributor(self):
        pass

    def card(self):
        pass

    def center_click(self):
        center = self.program.data.get_center()
        self.click(center)

    # ToDo
    def course(self):
        pass

    def divert_1(self):
        pass

    def download_upload(self):
        pass

    def fuel(self):
        pass

    def leaves(self):
        pass

    # ToDo
    def manifolds(self):
        pass

    def sample(self):
        pass

    def scan(self):
        pass

    def shields(self):
        pass

    def simon_says(self):
        pass

    def trash(self):
        pass

    def vent(self):
        pass

    def wires(self):
        pass

    def kill(self):
        self.toggle_kill()
        while self.kill_status:
            # print("kill")
            key_press("q")
            if check_break():
                self.kill_status = False
            wait_seconds(0.1)
            self.program.window.update()
