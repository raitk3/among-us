from PIL import ImageGrab
import json
from pynput import mouse


class Data:
    def __init__(self, common):
        self.common = common
        self.rejoin_code = ""
        self.data = self.read_data_from_file()
        self.init_missing_data()
        self.write_data_to_file()

# MAIN

    def init_missing_data(self):
        self.data["coords"] = self.data.get("coords", [[510, 365], [965, 895], [910, 335], [1210, 340]])
        self.data["rejoin_cooldown"] = self.data.get("rejoin_cooldown", 3.0)
        self.data["display"] = self.data.get("display", [[0, 0], [1920, 1080]])
        self.data["rejoin_code"] = self.data.get("rejoin_code", "")

    def read_data_from_file(self):
        # print("Reading data from file.")
        try:
            with open("data.json", encoding='utf-8') as file:
                # print('"data.json" exists, woo.')
                return json.loads(file.read())
        except Exception:
            # print("File is missing, loading base stuff.")
            with open("data.json", "w", encoding='utf-8'):
                return {}

    def write_data_to_file(self):
        # print("Update the data file")
        with open("data.json", "w", encoding='utf-8') as file:
            json.dump(self.data, file)

# TASKS

    def get_screenshot(self):
        image = ImageGrab.grab(bbox=(self.data["display"][0][0],
                                     self.data["display"][0][1],
                                     self.data["display"][0][0] +
                                     self.data["display"][1][0],
                                     self.data["display"][0][1] + self.data["display"][1][1]))
        pixels = image.load()
        return pixels

    def get_coordinates(self):
        with mouse.Events() as events:
            for event in events:
                try:
                    if event.button == mouse.Button.left:
                        return [event.x, event.y]
                except Exception:
                    if self.common.check_break():
                        return tuple()
                    pass

    def get_center(self):
        return ((self.get_bottom_right()[0] + self.get_top_left()[0]) // 2,
                (self.get_bottom_right()[1] + self.get_top_left()[1]) // 2)

    def get_display_size(self):
        return (self.get_bottom_right()[0] - self.get_top_left()[0], self.get_bottom_right()[1] - self.get_top_left()[1])
    
    def get_scale(self):
        return min(self.get_display_size()) / 2

    def get_top_left(self):
        return self.data["display"][0]

    def set_top_left(self, coords):
        if len(coords) == 2:
            self.data["display"][0] = [int(el) for el in coords]

    def get_bottom_right(self):
        return self.data["display"][1]

    def set_bottom_right(self, coords):
        if len(coords) == 2:
            self.data["display"][1] = [int(el) for el in coords]

# REJOIN

    def get_cross_coords(self):
        return self.data["coords"][0]

    def get_textbox_1_coords(self):
        # print("Get coords for textbox")
        return self.data["coords"][1]

    def get_textbox_2_coords(self):
        # print("Get coords for textbox")
        return self.data["coords"][2]

    def get_arrow_coords(self):
        # print("Get coords for arrow")
        return self.data["coords"][3]

    def set_cross(self, coords):
        if len(coords) == 2:
            # print(f"Set cross coords to {coords}")
            self.data["coords"][0] = [int(el) for el in coords]

    def set_textbox_1(self, coords):
        if len(coords) == 2:
            # print(f"Set textbox coords to {coords}")
            self.data["coords"][1] = [int(el) for el in coords]

    def set_textbox_2(self, coords):
        if len(coords) == 2:
            # print(f"Set textbox coords to {coords}")
            self.data["coords"][2] = [int(el) for el in coords]

    def set_arrow(self, coords):
        if len(coords) == 2:
            # print(f"Set arrow coords to {coords}")
            self.data["coords"][3] = [int(el) for el in coords]

    def get_rejoin_code(self):
        return self.data["rejoin_code"]
    
    def set_rejoin_code(self, code):
        self.data["rejoin_code"] = code
        self.write_data_to_file()

    def set_rejoin_cooldown(self, cooldown):
        self.data["rejoin_cooldown"] = float(cooldown)
        self.write_data_to_file()

    def get_rejoin_cooldown(self):
        return self.data["rejoin_cooldown"]
  