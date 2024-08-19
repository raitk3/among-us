from tkinter import ttk
from subparts.common import State

class View():
    def __init__(self, ux) -> None:
        self.ux = ux
        self.window = self.ux.window
        self.common = self.ux.common
        self.data = self.ux.data
        self.style = ttk.Style()
        self.configure_style()
        for j in range(4):
            self.window.columnconfigure(j, weight=1, uniform='fourth')

    def configure_style(self):
        self.window.minsize(600, 100)
        self.window.maxsize(600, 1000)
        bg = "black"
        fg = "white"
        fg_disabled = "gray"
        fg_active = "red"
        active = "lime"
        self.font = ("Arial", 14)
        header_font = ("Arial Bold", 18)
        self.style.theme_use('clam')

        self.window.configure(bg="black")

        self.style.configure("Borderless.TLabel",
                             background=bg,
                             foreground=bg,
                             relief="flat",
                             font=header_font,
                             )
        self.style.configure("Header.TLabel",
                             background=bg,
                             foreground=fg,
                             font=header_font,
                             relief="raised")

        self.style.configure("Normal.TLabel",
                             background=bg,
                             foreground=fg,
                             font=self.font,
                             relief="raised")

        self.style.configure("About.TLabel",
                             background=bg,
                             foreground=fg,
                             font=self.font)

        self.style.configure("Normal.TButton",
                             background=bg,
                             foreground=fg,
                             font=self.font
                             )
        
        self.style.configure("Active.TButton",
                             background=bg,
                             foreground=fg_active,
                             font=self.font
                             )

        self.style.configure("Disabled.TButton",
                             background=bg,
                             foreground=fg_disabled,
                             font=self.font
                             )

        self.style.map('TButton', foreground=[
                       ('active', active)], background=[('active', bg)])

        self.style.configure("Normal.TEntry",
                             background=bg,
                             foreground=fg,
                             fieldbackground=bg
                             )

        self.style.map('Normal.TCombobox', fieldbackground=[('readonly', bg)])
        self.style.map('Normal.TCombobox', selectbackground=[('readonly', bg)])
        self.style.map('Normal.TCombobox', selectforeground=[('readonly', fg)])
        self.style.configure('TCombobox', foreground=fg, background=bg, font=self.font)

        self.style.layout('Normal.TSpinbox', [('Spinbox.field',
                                               {'expand': 1,
                                                'sticky': 'nswe',
                                                'children': [('null',
                                                              {'side': 'right',
                                                               'sticky': 'ns',
                                                               'children': [('Spinbox.uparrow', {'side': 'top', 'sticky': 'e'}),
                                                                            ('Spinbox.downarrow', {'side': 'bottom', 'sticky': 'e'})]}),
                                                             ('Spinbox.padding',
                                                              {'sticky': 'nswe',
                                                               'children': [('Spinbox.textarea', {'sticky': 'nswe'})]})]})])

        self.style.configure("Normal.TSpinbox",
                             background=fg,
                             foreground=fg,
                             fieldbackground=bg,
                             arrowsize=17)

    def on_entry(self):
        pass

    def update(self):
        pass

    def on_exit(self):
        for child in self.window.winfo_children():
            child.destroy()

    def redraw(self):
        self.on_exit()
        self.on_entry()

    # Other functions
    def add_header(self, title):
        # print("Adding header")
        if len(self.ux.get_all_states()) > 1:
            # print("The states list is longer than 1, so I could go back...add Back button")
            ttk.Button(self.window, text="Back", style="Normal.TButton", command=lambda: self.ux.set_all_states(self.ux.get_all_states()[:-1])).grid(
                row=0, column=0, sticky="NESW")
        else:
            ttk.Button(self.window, text="About", style="Normal.TButton", command=lambda: self.ux.set_state(
                State.ABOUT)).grid(row=0, column=0, sticky="NESW")

        # print(f"The title is '{title}'")
        ttk.Label(self.window, style="Header.TLabel", text=title.upper(), anchor="center").grid(
            row=0, column=1, columnspan=2, rowspan=2, sticky="NESW")
        ttk.Label(self.window, style="Borderless.TLabel",
                  text="l").grid(row=1, column=0, sticky="NEWS")
        if self.ux.get_current_state() not in [State.SETTINGS]:
            # print("It's not Settings nor menu, so let's add Settings button, too")
            ttk.Button(self.window, text="Settings", style="Normal.TButton", command=lambda: self.ux.set_state(State.SETTINGS)).grid(
                row=0, column=3, sticky="NESW")

    def add_buttons(self, buttons, from_row, columnspan, columns=1, kill_enabled=False):
        for i, el in enumerate(buttons):
            com, enabled = buttons[el]
            if el == "COVID" and kill_enabled:
                ttk.Button(self.window, text=el, style="Active.TButton",
                        command=com, state='enabled').grid(
                    row=from_row + (i // columns), column=(i*columnspan) % (columns*columnspan), sticky="NESW", columnspan=columnspan)
            elif enabled:
                ttk.Button(self.window, text=el, style="Normal.TButton",
                        command=com, state='enabled').grid(
                    row=from_row + (i // columns), column=(i*columnspan) % (columns*columnspan), sticky="NESW", columnspan=columnspan)
            else:
                ttk.Button(self.window, text=el, style="Disabled.TButton",
                        command=com, state='disabled').grid(
                    row=from_row + (i // columns), column=(i*columnspan) % (columns*columnspan), sticky="NESW", columnspan=columnspan)

    def clear_window(self):
        # print("Let's clear everything")
        for el in self.window.winfo_children():
            el.destroy()