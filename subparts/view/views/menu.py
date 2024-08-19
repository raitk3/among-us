from subparts.view.view import View
from subparts.common import State

class Menu(View):
    def __init__(self, ux) -> None:
        super().__init__(ux)

    def on_entry(self):
        menu_items = {
            "Join a lobby": (lambda: self.ux.set_state(State.JOIN), True),
            "Tasks": (lambda: self.ux.set_state(State.TASKS), True),
        }
        self.add_header("Among Us Toolkit")
        self.add_buttons(menu_items, 2, 2, 2)
