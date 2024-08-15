from subparts.view.view import View
from subparts.common import State

import tkinter as tk
from tkinter import ttk

class Join(View):
    def __init__(self, ux) -> None:
        super().__init__(ux)

    def on_entry(self):
        self.add_header("Join a lobby")
        coords = []
        origin_x, origin_y = 2, 0

        ttk.Label(self.window, style="Normal.TLabel", text="Code").grid(
            row=origin_x + 1, column=origin_y, sticky="NEWS")

        tb = ttk.Entry(self.window, style="Normal.TEntry", font=self.font)
        tb.insert(10, self.data.get_rejoin_code())
        tb.grid(row=origin_x + 1, column=origin_y + 1, sticky="NESW",
                columnspan=2, padx=1, pady=1)
        ttk.Button(self.window, text="Join", style="Normal.TButton", command=lambda code=tb: [self.data.set_rejoin_code(tb.get()), self.rejoin()]).grid(
            row=origin_x + 1, column=origin_y + 3, sticky="NESW")
        ttk.Label(self.window, style="Normal.TLabel", text="To stop autojoin, press Esc or Shift", anchor='center').grid(
        row=origin_x + 2, column=0, columnspan=4, sticky="NEWS")
        
    def rejoin(self):
        code = self.data.get_rejoin_code()
        # print("Rejoin code is: ", self.rejoin_code)
        while True:
            self.common.wait_seconds(0.2)
            if self.common.check_break():
                # print("Shift was pressed, stop it!")
                break
            # print("Click cross")
            self.common.click(self.data.get_cross_coords())
            self.common.wait_seconds(0.2)
            # print("Click textbox 1")
            self.common.click(self.data.get_textbox_1_coords())
            self.common.wait_seconds(0.2)
            # print("Click textbox 2")
            self.common.click(self.data.get_textbox_2_coords())
            self.common.wait_seconds(0.2)
            # print("Write the code")
            self.common.write(code)
            # print("Press the arrow")
            self.common.wait_seconds(0.1)
            self.common.click(self.data.get_arrow_coords())
            self.common.wait_seconds(self.data.get_rejoin_cooldown())