from subparts.view.view import View
from tkinter import ttk
from subparts.common import Coordinate


class Settings(View):
    def __init__(self, ux) -> None:
        super().__init__(ux)
        self.data = ux.data

    def on_entry(self):
        self.add_header("Settings")
        buttons = {
            "TOP LEFT": (lambda: self.get_new_coords(Coordinate.TOP_LEFT), "Get coords"),
            "BOTTOM RIGHT": (lambda: self.get_new_coords(Coordinate.BOTTOM_RIGHT), "Get coords"),
            "DISPLAY SIZE": None,
            "CENTER": None,
            "CROSS": (lambda: self.get_new_coords(Coordinate.CROSS), "Get coords"),
            "TEXTBOX 1": (lambda: self.get_new_coords(Coordinate.TB_1), "Get coords"),
            "TEXTBOX 2": (lambda: self.get_new_coords(Coordinate.TB_2), "Get coords"),
            "ARROW": (lambda: self.get_new_coords(Coordinate.ARROW), "Get coords"),
            "REJOIN COOLDOWN": None
        }
        self.coords = []
        self.cooldowns = []
        origin_x, origin_y = 2, 0
        origin = self.data.get_top_left()
        display_size = self.data.get_bottom_right()
        cross = self.data.get_cross_coords()
        textbox_1 = self.data.get_textbox_1_coords()
        textbox_2 = self.data.get_textbox_2_coords()
        arrow = self.data.get_arrow_coords()

        ttk.Button(self.window, text="Save", style="Normal.TButton", command=lambda : self.save_settings()).grid(row=0, column=3, sticky="NEWS")
        for j, data_element in enumerate(buttons):
            ttk.Label(
                self.window, style="Normal.TLabel", text=data_element.capitalize()).grid(row=origin_x + j + 1, column=origin_y, sticky="NESW")
            ttk.Label(
                self.window, style="Normal.TLabel", text=data_element.capitalize()).grid(row=origin_x + j + 1, column=origin_y, sticky="NESW")
            if j in range(0, 2) or j in range(4, 8):
                for i in range(2):

                    tb = ttk.Entry(
                        self.window, style="Normal.TEntry", width = 1, font=self.font)
                    self.coords.append(tb)
                    if data_element == "CROSS":
                        tb.insert(10, string=cross[i % 2])
                    elif data_element == "TEXTBOX 1":
                        tb.insert(10, string=textbox_1[i % 2])
                    elif data_element == "TEXTBOX 2":
                        tb.insert(10, string=textbox_2[i % 2])
                    elif data_element == "ARROW":
                        tb.insert(10, string=arrow[i % 2])
                    elif data_element == "BOTTOM RIGHT":
                        tb.insert(10, string=display_size[i % 2])
                    elif data_element == "TOP LEFT":
                        tb.insert(10, string=origin[i % 2])
                    tb.grid(row=origin_x + j+1, column=origin_y + i + 1,
                            sticky="NESW", padx=1, pady=1)
                ttk.Button(self.window, text=buttons[data_element][1],
                           style="Normal.TButton",
                           # state="disabled",
                           command=buttons[data_element][0]).grid(
                    row=origin_x + j + 1, column=origin_y + 3, sticky="NESW")
            elif j in range(2, 4):
                if j == 2:
                    text = self.data.get_display_size()
                else:
                    text = self.data.get_center()
                label_x = ttk.Label(
                    self.window, style="Normal.TLabel", text=text[0]
                    ).grid(row=origin_x + j + 1, column=origin_y + 1, sticky="NESW")
                label_y = ttk.Label(
                    self.window, style="Normal.TLabel", text=text[1]
                    ).grid(row=origin_x + j + 1, column=origin_y + 2, sticky="NESW")
            elif j == 8:
                spinbox = ttk.Spinbox(self.window,
                                        values=[l / 10 for l in range(1, 100)],
                                        style="Normal.TSpinbox",
                                        font=self.font
                                        )
                self.cooldowns.append(spinbox)

                spinbox.insert(0, self.data.get_rejoin_cooldown())

                spinbox.grid(row=origin_x + j+1, column=origin_y + 1,
                                padx=1, pady=1, columnspan=3, sticky="NEWS")
                
    def save_settings(self):
        coordinates = [el.get() for el in self.coords]
        cds = [el.get() for el in self.cooldowns]
        self.data.set_top_left(coordinates[:2])
        self.data.set_bottom_right(coordinates[2:4])
        self.data.set_cross(coordinates[4:6])
        self.data.set_textbox_1(coordinates[6:8])
        self.data.set_textbox_2(coordinates[8:10])
        self.data.set_arrow(coordinates[10:12])
        self.data.set_rejoin_cooldown(cds[0])
        self.data.write_data_to_file()