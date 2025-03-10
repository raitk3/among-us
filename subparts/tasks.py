from subparts.common import *

class Task:
    def __init__(self, label, command, maps, enabled, use_button) -> None:
        self.label = label
        self.command = command
        self.maps = maps
        self.enabled = enabled
        self.use_button = use_button
        

class Tasks:
    def __init__(self, program):
        self.program = program
        self.common = self.program.common
        self.data = self.common.data
        self.kill_status = False
        self.current_map = Map.SKELD
        self.tasks = [
            # command, maps, enabled, usebutton
            Task("Align", lambda: self.align(), [Map.SKELD], True, True),
            Task("Align telescope", lambda: self.align_telescope(), [Map.POLUS], False, True),
            Task("Assemble artifact", lambda: self.assemble_artifact(), [Map.MIRA, Map.FUNGLE], False, True),
            Task("Asteroids", lambda: self.asteroids(), [Map.SKELD, Map.MIRA, Map.POLUS], False, True),
            Task("Build sandcastle", lambda: self.sandcastle(), [Map.FUNGLE], False, True),
            Task("Buy beverage", lambda: self.beverage(), [Map.MIRA], False, True),
            Task("Calibrate distributor", lambda: self.calibrate_distributor(), [Map.SKELD, Map.AIRSHIP], True, True),
            Task("Catch fish", lambda: self.fish(), [Map.FUNGLE], False, True),
            Task("Chart course",lambda: self.course(), [Map.SKELD, Map.MIRA, Map.POLUS], False, True),
            Task("Clean toilet",lambda: self.toilet(), [Map.AIRSHIP], False, True),
            Task("Clean vent",lambda: self.vent(), [Map.SKELD], False, True),
            Task("Collect samples",lambda: self.sample_fungle(), [Map.FUNGLE], False, True),
            Task("Collect shells",lambda: self.shell(), [Map.FUNGLE], False, True),
            Task("Collect vegetables",lambda: self.vegetables(), [Map.FUNGLE], False, True),
            Task("Crank generator",lambda: self.generator(), [Map.FUNGLE], False, True),
            Task("Decontaminate",lambda: self.scan(), [Map.AIRSHIP], True, True),
            Task("Develop photos",lambda: self.photos(), [Map.AIRSHIP], False, True),
            Task("Divert 1", lambda: self.divert_1(), [Map.SKELD, Map.MIRA, Map.AIRSHIP], True, True),
            Task("Divert 2", lambda: self.center_click(), [Map.SKELD, Map.MIRA, Map.AIRSHIP], True, True),
            Task("Download/Upload", lambda: self.download_upload(), [Map.SKELD, Map.POLUS], True, True),
            Task("Download", lambda: self.download_mira(), [Map.MIRA], False, True),
            Task("Enter ID-code", lambda: self.id_code(), [Map.MIRA, Map.AIRSHIP, Map.FUNGLE], False, True),
            Task("Extract fuel", lambda: self.extract(), [Map.MIRA, Map.AIRSHIP, Map.FUNGLE], False, True),
            Task("Fill canisters", lambda: self.canisters(), [Map.POLUS], False, True),
            Task("Find signal", lambda: self.signal(), [Map.FUNGLE], False, True),
            Task("Fix antenna", lambda: self.antenna(), [Map.FUNGLE], False, True),
            Task("Fix node 1", lambda: self.node_1(), [Map.POLUS], False, True),
            Task("Fix node 2", lambda: self.node_2(), [Map.POLUS], False, True),
            Task("Fix shower", lambda: self.antenna(), [Map.AIRSHIP], False, True),
            Task("Fix wiring", lambda: self.wires(), [Map.SKELD, Map.MIRA, Map.POLUS, Map.AIRSHIP, Map.FUNGLE], True, True),
            Task("Fuel engines", lambda: self.fuel(), [Map.SKELD, Map.MIRA, Map.POLUS, Map.AIRSHIP, Map.FUNGLE], True, True),
            Task("Help critter", lambda: self.critter(), [Map.FUNGLE], False, True),
            Task("Hoist supplies", lambda: self.hoist(), [Map.FUNGLE], False, True),
            Task("Insert keys", lambda: self.keys(), [Map.POLUS], False, True),
            Task("Inspect sample", lambda: self.sample(), [Map.SKELD, Map.POLUS], False, True),
            Task("Leaves", lambda: self.leaves(), [Map.SKELD, Map.MIRA], False, True),
            Task("Lift weights", lambda: self.gym(), [Map.FUNGLE], False, True),
            Task("Make burger", lambda: self.burger(), [Map.AIRSHIP], False, True),
            Task("Measure weather", lambda: self.weather(), [Map.MIRA], False, True),
            Task("Mine ores", lambda: self.mine(), [Map.FUNGLE], False, True),
            Task("Monitor mushroom", lambda: self.mushroom(), [Map.FUNGLE], False, True),
            Task("Monitor tree", lambda: self.tree(), [Map.POLUS], False, True),
            Task("Open waterways", lambda: self.open_water(), [Map.POLUS], False, True),
            Task("Pick up towels 1", lambda: self.towels_1(), [Map.AIRSHIP], False, True),
            Task("Pick up towels 2", lambda: self.towels_2(), [Map.AIRSHIP], False, True),
            Task("Put away pistols", lambda: self.guns_1(), [Map.AIRSHIP], False, True),
            Task("Put away rifles", lambda: self.guns_2(), [Map.AIRSHIP], False, True),
            Task("Play video game", lambda: self.asteroids(), [Map.FUNGLE], False, True),
            Task("Polish a rock", lambda: self.gem(), [Map.AIRSHIP, Map.FUNGLE], False, True),
            Task("Reboot WiFi 1", lambda: self.wifi_1(), [Map.POLUS], False, True),
            Task("Reboot WiFi 2", lambda: self.wifi_2(), [Map.POLUS], False, True),
            Task("Record temperature", lambda: self.temps(), [Map.POLUS], False, True),
            Task("Repair drill", lambda: self.drill(), [Map.POLUS], True, True),
            Task("Replace parts", lambda: self.parts(), [Map.POLUS], False, True),
            Task("Replace water jug", lambda: self.water(), [Map.POLUS, Map.FUNGLE], False, True),
            Task("Reset breakers", lambda: self.start_task(), [Map.AIRSHIP], False, True),
            Task("Rewind tapes", lambda: self.start_task(), [Map.AIRSHIP], False, True),
            Task("Roast marshmallow", lambda: self.start_task(), [Map.AIRSHIP], False, True),
            Task("Run diagnostics", lambda: self.start_task(), [Map.MIRA], False, True),
            Task("Scan", lambda: self.scan(), [Map.SKELD, Map.MIRA, Map.POLUS], True, True),
            Task("Scan boarding pass", lambda: self.start_task(), [Map.POLUS], False, True),
            Task("Shields", lambda: self.shields(), [Map.SKELD, Map.MIRA], False, True),
            Task("Sort records", lambda: self.start_task(), [Map.AIRSHIP], False, True),
            Task("Sort samples", lambda: self.start_task(), [Map.MIRA], False, True),
            Task("Stabilize steering", lambda: self.center_click(), [Map.SKELD, Map.AIRSHIP], True, True),
            Task("Start fans", lambda: self.start_task(), [Map.AIRSHIP], False, True),
            Task("Start reactor", lambda: self.simon_says(), [Map.SKELD, Map.MIRA, Map.POLUS], True, True),
            Task("Store artifacts", lambda: self.start_task(), [Map.POLUS], False, True),
            Task("Swipe card", lambda: self.card(), [Map.SKELD, Map.POLUS], True, True),
            Task("Throw frisbees", lambda: self.start_task(), [Map.FUNGLE], False, True),
            Task("Trash", lambda: self.trash(), [Map.SKELD, Map.MIRA, Map.POLUS, Map.AIRSHIP, Map.FUNGLE], True, True),
            Task("Unlock manifolds", lambda: self.manifolds(), [Map.SKELD, Map.MIRA, Map.POLUS], False, True),
            Task("Unlock safe", lambda: self.start_task(), [Map.AIRSHIP], False, True),
            Task("Water plants", lambda: self.start_task(), [Map.MIRA, Map.FUNGLE], False, True),
            Task("COVID", lambda: self.toggle_kill(), [Map.SKELD, Map.MIRA, Map.POLUS, Map.AIRSHIP, Map.FUNGLE], True, False)
        ]

    def get_filtered_tasks(self, map):
        return [task for task in self.tasks if map in task.maps]

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
            if self.commom.check_break():
                break

    def drag_slowly(self, scales_1, scales_2, steps):
        coords_1 = self.common.scale_to_coords(scales_1)
        coords_2 = self.common.scale_to_coords(scales_2)
        x_diff = (coords_2[0] - coords_1[0])
        y_diff = (coords_2[1] - coords_1[1])
        self.common.mouse.position = coords_1
        self.common.left_mouse_button(True)
        for _ in range(steps):
            self.common.mouse.move(x_diff//steps, y_diff//steps)
            self.common.wait_seconds(0.5 / steps)
        self.common.left_mouse_button(False)

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

    #####CYCLE#####
    def get_use_button(self):
        brc = self.data.get_bottom_right()
        s = self.data.get_scale()
        coeff = 0.27
        return (brc[0] - coeff*s, brc[1] - coeff*s)

    def start_task(self):
        self.center_click()
        self.click(self.get_use_button())
        self.common.wait_seconds(0.5)

    def do_task(self, task: Task):
        
        if task.use_button:
            self.start_task()
        task.command()
        if task.use_button:
            self.common.wait_seconds(2)

    #####TASKS#####
    def align(self):
        center = (0, 0)
        align_parabola_constant = 0.30887
        range_of_align_up_and_down_values = range(-7222, 7222, 100)
        # Tip of parabola (1330, 150)    => (0.6852, -0.7222)
        # Center of parabola (1243, 540) => (0.5241, 0)
        # Bottom of parabola (1330, 930) => (0.6852, 0.7222)
        image = self.get_screenshot()
        for y in range_of_align_up_and_down_values:
            y_scale = y / 10000
            x_scale = align_parabola_constant * y_scale ** 2 + 0.5241
            actual_scales = (center[0] + x_scale, center[1] + y_scale)
            coordinates = self.common.scale_to_coords(actual_scales)
            r, g, b = image[coordinates]
            if max(r, g, b) > 70:
                self.common.drag_from_center(actual_scales, center)
                break
            if self.common.check_break():
                break
    
    # ToDo
    def align_telescope(self):
        pass

    # ToDo
    def antenna(self):
        pass

    # ToDo
    def assemble_artifact(self):
        pass

    # ToDo       
    def asteroids(self):
        pass
        
    # ToDo
    def beverage(self):
        pass

    # ToDo
    def burger(self):
        pass

    def calibrate_distributor(self):
        box1 = (0.5, -0.574)
        button1 = (0.5, -0.426)
        box2 = (0.5, -0.074)
        button2 = (0.5, 0.074)
        box3 = (0.5, 0.4222)
        button3 = (0.5, 0.552)

        done = 0
        while done != 3:
            if self.common.check_break():
                break
            screenshot = self.get_screenshot()
            if done == 0 and screenshot[self.common.scale_to_coords(box1)][0] > 0:
                self.common.click_from_center(button1)
                done = 1
            elif done == 1 and screenshot[self.common.scale_to_coords(box2)][2] > 0:
                self.common.click_from_center(button2)
                done = 2
            elif done == 2 and screenshot[self.common.scale_to_coords(box3)][2] > 0:
                self.common.click_from_center(button3)
                done = 3
            if screenshot[self.common.scale_to_coords(box1)][0] == 0:
                done = 0
            print(done)

    # ToDo
    def canisters(self):
        pass

    # ToDo
    def critter(self):
        pass

    def card(self):
        self.click(self.common.scale_to_coords((-0.26823, 0.510417)))
        self.common.wait_seconds(1)
        if self.common.check_break():
            return
        self.drag_slowly((-0.8151, -0.21875),
                         (0.903646, -0.21875),
                         50)
        self.common.left_mouse_button(False)

    def center_click(self):
        self.click_from_center((0, 0))

    # ToDo
    def course(self):
        pass

    def divert_1(self):
        buttons = [
           (-0.627, 0.4555),
           (-0.4537, 0.4555),
           (-0.2759, 0.4555),
           (-0.0907, 0.4555),
           (0.0888, 0.4555),
           (0.2648, 0.4555),
           (0.4426, 0.4555),
           (0.6222, 0.4555)
        ]
        self.common.wait_seconds(0.2)
        image = self.get_screenshot()
        for button in buttons:
            if image[self.common.scale_to_coords(button)][0] > 120:
                self.common.drag_from_center(button, (button[0], 0))

    def download_upload(self):
        self.click_from_center((0, 0.224))

    # ToDo
    def download_mira(self):
        pass

    def drill(self):
        corners = [
            (-0.3296, -0.60185),
            (-0.3296, 0.47777),
            (0.31666, -0.60185),
            (0.31666, 0.47777)
        ]
        for corner in corners:
            for _ in range(4):
                if self.common.check_break():
                    break
                self.click_from_center(corner)
                self.common.wait_seconds(0.1)
                
    # ToDo
    def extract(self):
        pass

    # ToDo
    def gem(self):
        pass

    # ToDo
    def guns_1(self):
        pass

    # ToDo
    def guns_2(self):
        pass

    # ToDo
    def gym(self):
        pass

    # ToDo
    def fish(self):
        pass

    def fuel(self):
        self.common.hold_from_center((0.93, 0.6146))
        self.common.wait_seconds(3.5)
        self.common.mouse.release(mouse.Button.left)

    # ToDo
    def generator(self):
        pass

    # ToDo
    def hoist(self):
        pass

    # ToDo
    def id_code(self):
        pass

    # ToDo
    def keys(self):
        pass

    # ToDo
    def leaves(self):
        pass

    # ToDo
    def manifolds(self):
        pass

    # ToDo
    def mine(self):
        pass

    # ToDo
    def mushroom(self):
        pass

    #ToDo
    def node_1(self):
        pass

    # ToDo
    def node_2(self):
        pass

    # ToDo
    def open_water(self):
        pass

    # ToDo
    def parts(self):
        pass

    # ToDo
    def photos(self):
        pass

    # ToDo
    def sample(self):
        pass

    # ToDo
    def sample_fungle(self):
        pass

    # ToDo
    def sandcastle(self):
        pass

    def scan(self):
        pass

    # ToDo
    def shell(self):
        pass

    # ToDo
    def shields(self):
        pass

    # ToDo
    def signal(self):
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
            order_to_press = []
            while len(order_to_press) < i:
                image = self.get_screenshot()
                for j, light in enumerate(lights):
                    if self.common.check_break():
                        return
                    if image[self.common.scale_to_coords((light[0], light[1]))][2] != 0:
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

    # ToDo
    def temps(self):
        pass

    # ToDo
    def toilet(self):
        pass

    # ToDo
    def towels_1(self):
        pass

    # ToDo
    def towels_2(self):
        pass

    def trash(self):
        self.common.drag_from_center((0.565, -0.21875), (0.565, 0.302), 2)

    # ToDo
    def tree(self):
        pass

    # ToDo
    def vegetables(self):
        pass

    # ToDo
    def vent(self):
        pass

    # ToDo
    def water(self):
        pass

    # ToDo
    def weather(self):
        pass

    # ToDo
    def wifi_1(self):
        pass

    # ToDo
    def wifi_2(self):
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
        print("Q")
        self.common.key_press("q")
    
    def toggle_kill(self):
        self.program.views["TASKS"].toggle_kill()
