from subparts.view.view import View
import tkinter as tk
from tkinter import ttk
from subparts.common import Map


class Tasks(View):
    def __init__(self, ux) -> None:
        super().__init__(ux)
        self.tasks = self.ux.tasks
        self.drawn_map = Map.SKELD
        self.current_map = tk.StringVar()
        self.kill_active = False
        self.update_needed = False

    def on_entry(self):
        origin_x, origin_y = 2, 0
        self.add_header("Tasks")
        self.cb = ttk.Combobox(self.window, values=[map.name for map in Map], state="readonly", textvariable=self.current_map, style="Normal.TCombobox", justify="center")
        self.cb.set(self.drawn_map.name)
        self.cb.grid(row=origin_x + 1, column=origin_y, columnspan=4, sticky="NESW")

        self.draw()
    
    def draw(self):
        tasks_with_start = {}
        for task in self.tasks.get_filtered_tasks(self.drawn_map):
            def com(t=task): return self.tasks.do_task(t)
            en = task.enabled
            tasks_with_start[task.label] = (com, en)
        self.add_buttons(tasks_with_start, 4, 1, 4, kill_enabled=self.kill_active)

    def update(self):
        self.check_update_needed()
        current_choice = Map.from_string(self.current_map.get())
        if self.update_needed:
            self.drawn_map = current_choice
            self.on_exit()
            self.on_entry()
            self.update_needed = False
        if self.kill_active:
            if self.common.check_break():
                self.toggle_kill(False)
            else:
                self.tasks.kill()
                self.common.wait_seconds(0.02)

    def check_update_needed(self):
        current_choice = Map.from_string(self.current_map.get())
        if current_choice != self.drawn_map:
            self.update_needed = True
    
    def toggle_kill(self, value=None):
        if value != None:
            self.kill_active = value
        else:
            self.kill_active = not self.kill_active
        self.update_needed = True
