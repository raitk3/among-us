from PIL import ImageGrab
import json
from pynput import mouse, keyboard

from subparts.common import *

class Data:
    def __init__(self, m=None, kb=None):
        self.rejoin_code = ""
        self.data = self.read_data_from_file()
        self.sentences = self.data["sentences"]
        self.keyboard = kb if kb != None else keyboard.Controller()
        self.mouse = m if m != None else mouse.Controller()
        self.current_pack = 0

    def get_screenshot(self):
        image = ImageGrab.grab(bbox=(self.data["display"][0][0],
                                     self.data["display"][0][1],
                                     self.data["display"][0][0] +
                                     self.data["display"][1][0],
                                     self.data["display"][0][1] + self.data["display"][1][1]))
        pixels = image.load()
        return pixels

    def correct_coords(self, coords, subtract=False):
        if subtract:
            return (int(coords[0]) - int(self.get_origin()[0]), int(coords[1]) - int(self.get_origin()[1]))
        return (int(coords[0]) + int(self.get_origin()[0]), int(coords[1]) + int(self.get_origin()[1]))

    def click(self, coords, m=None):
        m = m if m != None else mouse.Controller()
        m.position = self.correct_coords(coords)
        m.click(mouse.Button.left)
        wait_seconds(0.2)

    def get_coordinates(self, subtract=True):
        with mouse.Events() as events:
            for event in events:
                try:
                    if event.button == mouse.Button.left:
                        if subtract:
                            return self.correct_coords((event.x, event.y), True)
                        return [event.x, event.y]
                except Exception:
                    if check_break():
                        return tuple()
                    pass

    def get_center(self):
        return [el//2 for el in self.get_display_size()]

    def read_data_from_file(self):
        # print("Reading data from file.")
        try:
            with open("data.json", encoding='utf-8') as file:
                # print('"data.json" exists, woo.')
                return json.loads(file.read())
        except Exception:
            # print("File is missing, loading base stuff.")
            with open("data.json", "w", encoding='utf-8'):
                return {
                    "coords": [[330, 320], [680, 650], [680, 550], [860, 650]],
                    "cooldowns": [3.0, 0.2],
                    "display": [[0, 0], [1366, 768]],
                    "sentences": [
                        ["S1", ["Sentence", "packet", "1"]]
                    ]
                }

    def write_data_to_file(self):
        # print("Update the data file")
        with open("data.json", "w", encoding='utf-8') as file:
            json.dump(self.data, file)

    def add_sentence(self, program, pack_to_add, textboxes):
        # print(f"Add another sentence to {pack_to_add}")
        self.save(pack_to_add, [el.get() for el in textboxes])
        self.sentences[int(pack_to_add)][1].append("")
        program.draw()

    def remove_sentence(self, program, pack_to_remove, textboxes):
        # print(f"Remove a sentence from {pack_to_remove}")
        self.save(pack_to_remove, [el.get() for el in textboxes])
        if len(self.get_sentences_pack(pack_to_remove)) > 1:
            # print("    More than 1 sentence, can do")
            self.save(pack_to_remove, [el.get() for el in textboxes[:-1]])
        else:
            pass
            # print("    But I don't have enough sentences...")
        program.draw()

    def add_sentence_pack(self):
        self.sentences.append(
            [len(self.sentences), ["Sentence"]])
        self.current_pack = len(self.sentences)-1

    def remove_current_sentence_pack(self):
        if len(self.sentences) > 1:
            self.sentences.remove(self.current_pack)
        self.current_pack = max(len(self.sentences)-1, 0)

    def get_sentences_pack(self, pack_to_get):
        # print(f"Get sentences for {pack_to_get}")
        return self.sentences[pack_to_get][1]

    def set_next_pack(self):
        self.current_pack += 1
        self.current_pack %= len(self.sentences)

    def set_previous_pack(self):
        self.current_pack -= 1
        self.current_pack %= len(self.sentences)

    def get_headers(self):
        return [el[0] for el in self.sentences]

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

    def get_current_pack(self):
        # print("Get currently used sentence pack.")
        return self.current_pack

    def set_current_pack(self, new_pack, event=None):
        # print(f"Set current map to {new_pack}")
        self.current_pack = int(new_pack)

    def rename_current_pack(self, new_name):
        # print(f"Renaming pack {self.current_pack} to {new_name}.")
        self.sentences[self.current_pack][0] = new_name

    def get_cooldown(self):
        # print("Get current cooldown for chat")
        try:
            return self.data["cooldowns"][0]
        except Exception:
            # print("    Oh f...the cooldowns missing from data_file, let's add it to it.")
            self.data["cooldowns"] = [3.0, 0.2]
            return self.data["cooldowns"][0]

    def set_cooldown(self, cooldown):
        # print(f"Set chat cooldown to {cooldown}")
        self.data["cooldowns"][0] = float(cooldown)
        self.write_data_to_file()

    def get_enter_cooldown(self):
        # print("Get cooldown for pressing enter after writing.")
        try:
            return self.data["cooldowns"][1]
        except Exception:
            # print("    Oh f...the cooldowns are missing from data file, let's add it to it.")
            self.data["cooldowns"] = [3.0, 0.2]
            return self.data["cooldowns"][1]

    def set_enter_cooldown(self, cooldown):
        # print("Setting enter cooldown to ", cooldown)
        self.data["cooldowns"][1] = float(cooldown)
        self.write_data_to_file()

    def get_origin(self):
        return self.data["display"][0]

    def set_origin(self, coords):
        if len(coords) == 2:
            self.data["display"][0] = [int(el) for el in coords]

    def get_display_size(self):
        return self.data["display"][1]

    def set_display_size(self, coords):
        if len(coords) == 2:
            self.data["display"][1] = [int(el) for el in coords]

    def save(self, map_to_save, sentences):
        # print(f"Save the sentences for {map_to_save}")
        self.sentences[int(map_to_save)][1] = sentences
        self.write_data_to_file()

    def send(self, current_pack, textboxes):
        sentences = [el.get().encode('utf-8') for el in textboxes]
        cooldowns = (self.get_cooldown(), self.get_enter_cooldown())
        self.save(current_pack, sentences)
        # print("The sentences are:")
        # print(*sentences, sep="\n")
        for sentence in sentences:
            wait_seconds(cooldowns[0])
            if check_break():
                # print("Shift was pressed, stooooop!")
                break
            # print("Writing:", sentence)
            write(sentence, self.keyboard)
            wait_seconds(cooldowns[1])
            # print("SEND IT!")
            key_press(keyboard.Key.enter, self.keyboard)

    def rejoin(self, window, code):
        self.rejoin_code = code[0].get().upper()
        # print("Rejoin code is: ", self.rejoin_code)
        while True:
            wait_seconds(2)
            if check_break():
                # print("Shift was pressed, stop it!")
                break
            # print("Click cross")
            self.click(self.data["coords"][0], self.mouse)
            wait_seconds(0.2)
            # print("Click textbox 1")
            self.click(self.data["coords"][1], self.mouse)
            wait_seconds(0.2)
            # print("Click textbox 2")
            self.click(self.data["coords"][2], self.mouse)
            wait_seconds(0.2)
            # print("Write the code")
            write(self.rejoin_code, self.keyboard)
            # print("Press the arrow")
            wait_seconds(0.1)
            self.click(self.data["coords"][3], self.mouse)

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
