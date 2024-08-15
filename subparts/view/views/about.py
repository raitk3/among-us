from subparts.view.view import View
import tkinter as tk
from tkinter import ttk

class About(View):
    def __init__(self, ux) -> None:
        super().__init__(ux)

    def on_entry(self):
        self.add_header("About")
        data = {
            "Version": self.ux.version + "_" + self.ux.version_type if len(self.ux.version_type) > 0 else self.ux.version,
            "Author": "sBYTEr"
        }
        for i, el in enumerate(data):
            ttk.Label(self.window, text=el+":", style="About.TLabel",
                      anchor="e").grid(row=i+2, column=0, columnspan=2, sticky="NEWS")
            ttk.Label(self.window, text=" " + data[el], style="About.TLabel", anchor="w").grid(
                row=i+2, column=2, columnspan=2, sticky="NEWS")