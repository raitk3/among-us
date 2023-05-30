from subparts.common import *

class Tasks:
    def __init__(self, program):
        self.program = program
        self.common = self.program.common
        self.data = self.common.data
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
            "Download/Upload": (lambda: self.download_upload(), True, True),
            "Fix wiring": (lambda: self.wires(), True, True),
            "Fuel engines": (lambda: self.fuel(), True, True),
            "Inspect sample": (lambda: self.sample(), False, True),
            "Leaves": (lambda: self.leaves(), False, True),
            "Scan": (lambda: self.scan(), True, True),
            "Shields": (lambda: self.shields(), False, True),
            "Stabilize steering": (lambda: self.center_click(), True, True),
            "Start reactor": (lambda: self.simon_says(), True, True),
            "Swipe card": (lambda: self.card(), False, True),
            "Trash": (lambda: self.trash(), True, True),
            "Unlock manifolds": (lambda: self.manifolds(), False, True),
            "COVID": (lambda: self.kill(), True, False)
        }

    #####HELP######

    def get_screenshot(self):
        return self.program.data.get_screenshot()

    def click(self, coords):
        self.common.click(coords)
    
    def click_from_center(self, coords):
        self.common.click_from_center(coords)

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
        lights = [(-0.8932 + i*0.078125, -0.415) for i in range(5)]
        count = 0

        while count < 1:
            if self.common.check_break():
                break
            image = self.get_screenshot()
            for i, light in enumerate(lights):
                if image[self.common.scale_to_coords((light[0], light[1]))][1] > 175:
                    # print(f"{i}: on")
                    count += 1
                else:
                    # print(f"{i}: off")
                    break
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


    def get_use_button(self):
        brc = self.data.get_bottom_right_corner()
        s = self.data.get_scale()
        coeff = 0.27
        return (brc[0] - coeff*s, brc[1] - coeff*s)

    def start_task(self):
        self.click((10, 10))
        self.click(self.get_use_button())
        self.common.wait_seconds(0.5)

    def do_task(self, task_to_do):
        task = self.tasks[task_to_do]
        if task[2]:
            self.start_task()
        task[0]()
        if task[2]:
            self.common.wait_seconds(2)

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
        self.click_from_center((0, 0))

    # ToDo
    def course(self):
        pass

    def divert_1(self):
        pass

    def download_upload(self):
        self.click_from_center((0, 0.224))

    def fuel(self):
        self.common.hold_from_center((0.93, 0.6146))
        self.common.wait_seconds(3.5)
        self.common.mouse.release(mouse.Button.left)

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
        lights = []
        buttons = []
        for i in range(3):
            spacing = 0.233
            row = -0.1146 + i*spacing
            for j in range(3):
                column = -0.8145 + j*spacing
                lights.append((column, row))
            for j in range(3):
                column = 0.33073 + j*spacing
                buttons.append((column, row))
        i = self.check_simon_lights()
        print(i)
        while i < 6:
            # print(i)
            order_to_press = []
            while len(order_to_press) < i:
                image = self.get_screenshot()
                for j, light in enumerate(lights):
                    if self.common.check_break():
                        return
                    if image[self.common.scale_to_coords((light[0], light[1]))] != (0, 0, 0):
                        order_to_press.append(buttons[j])
                        self.common.wait_seconds(0.25)
                print(order_to_press)
            print([buttons.index(element) for element in order_to_press])
            self.common.wait_seconds(0.5)
            for button in order_to_press:
                if self.common.check_break():
                    return
                self.click_from_center(button)
                image = self.get_screenshot()
                if image[self.common.scale_to_coords((button[0], button[1]))] == (189, 43, 0):
                    i = 0
            i += 1
        


    def trash(self):
        self.common.drag_from_center((0.565, -0.21875), (0.565, 0.302), 2)

    def vent(self):
        pass

    def wires(self):
        x = [-0.737, 0.667]
        y = [-0.4974, -0.15104, 0.1927, 0.53646]
        image = self.get_screenshot()
        for i in range(4):
            wire_color = image[self.common.scale_to_coords((x[0], y[i]))]
            for j in range(4):
                other_wire = image[self.common.scale_to_coords((x[1], y[j]))]
                if wire_color == other_wire:
                    self.common.drag_from_center((x[0], y[i]), (x[1], y[j]))
                    break

    def kill(self):
        self.toggle_kill()
        while self.kill_status:
            # print("kill")
            self.common.key_press("q")
            if self.common.check_break():
                self.kill_status = False
            self.common.wait_seconds(0.1)
            self.program.window.update()
