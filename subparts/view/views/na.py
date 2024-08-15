import tkinter as tk
from tkinter import ttk
from subparts.common import State

from subparts.view.view import View

class NA(View):
    def __init__(self, ux) -> None:
        super().__init__(ux)

    def on_entry(self):
        print("Uhhh...?")
        return super().on_entry()