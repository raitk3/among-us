import tkinter as tk
from tkinter import ttk
import os
import keyboard
import time


def wait_seconds(seconds: float):
    time_start = time.time()
    while (time.time() - time_start < seconds):
        if keyboard.is_pressed('shift'):
            break


class Data:
    def __init__(self):
        self.rejoin_code = ""
        self.cross = (330, 320)
        self.textbox = (680, 700)
        self.arrow = (860, 700)
        self.sentences = self.read_sentences_from_file()

    def read_sentences_from_file(self):
        list_of_strings = []
        if os.path.exists("sentences.txt"):
            with open("sentences.txt", encoding='utf-8') as file:
                for line in file.readlines():
                    list_of_strings.append(line.strip())
            if len(list_of_strings) < 1:
                return [""]
            return list_of_strings
        with open("sentences.txt", "w", encoding='utf-8'):
            return [""]

    def write_sentences_to_file(self):
        with open("sentences.txt", "w", encoding='utf-8') as file:
            for i, el in enumerate(self.sentences):
                if i != len(self.sentences):
                    el = el + "\n"
                file.write(el)

    def add_sentence(self, program, textboxes):
        self.save([el.get() for el in textboxes])
        self.sentences.append("")
        program.sentences()

    def remove_sentence(self, program, textboxes):
        self.save([el.get() for el in textboxes])
        if len(self.sentences) > 1:
            self.save([el.get() for el in textboxes[:-1]])
        program.sentences()

    def save(self, sentences):
        self.sentences = sentences
        self.write_sentences_to_file()

    def send(self, textboxes):
        self.save([el.get() for el in textboxes])
        for index, sentence in enumerate(self.sentences):
            wait_seconds(3)
            if keyboard.is_pressed('shift'):
                break
            print(sentence)
            keyboard.write(sentence)
            wait_seconds(0.1)
            print("SEND!")
            keyboard.send('enter')


class Program:
    def __init__(self, title):
        self.data = Data()
        self.window = tk.Tk()
        self.window.title(title)
        self.menu()

    def menu(self):
        self.clear_window()
        menu_items = {
            "Rejoin": lambda: self.rejoin(),
            "Sentences": lambda: self.sentences()
        }
        ttk.Label(self.window, text="What would you like to do?").grid(
            row=0, column=0, columnspan=2, sticky="NESW")
        self.add_buttons(menu_items, 1, 4)
        self.window.mainloop()

    def add_header(self, title):
        ttk.Button(self.window, text="Back", command=lambda: self.menu()).grid(
            row=0, column=0, sticky="NESW")
        ttk.Label(self.window, text=title).grid(
            row=0, column=1, columnspan=3, sticky="NESW")

    def sentences(self):
        self.clear_window()
        self.add_header("Sentences")
        textboxes = []
        for i, sentence in enumerate(self.data.sentences):
            ttk.Label(
                self.window, text=f"Sentence {i+1}").grid(row=i + 1, column=0, sticky="NESW")
            tb = ttk.Entry(self.window)
            textboxes.append(tb)
            tb.insert(10, string=self.data.sentences[i])
            tb.grid(row=i + 1, column=1, columnspan=3,
                    sticky="NESW", padx=1, pady=1)

        ttk.Button(self.window, text="Remove sentence", command=lambda textboxes=textboxes: self.data.remove_sentence(
            self, textboxes)).grid(row=len(self.data.sentences)+1, column=0, columnspan=2, sticky="NESW")
        ttk.Button(self.window, text="Add sentence", command=lambda textboxes=textboxes: self.data.add_sentence(
            self, textboxes)).grid(row=len(self.data.sentences)+1, column=2, columnspan=2, sticky="NESW")
        ttk.Button(self.window, text="Send!", command=lambda tb=textboxes: self.data.send(
            tb)).grid(row=len(self.data.sentences)+2, column=0, columnspan=4, sticky="NESW")
        for j in range(4):
            self.window.columnconfigure(j, weight=1, uniform='fourth')
        self.window.mainloop()

    def rejoin(self):
        self.clear_window()
        self.add_header("Rejoin")
        self.window.mainloop()

    def add_buttons(self, buttons, from_row, columnspan):
        for i, el in enumerate(buttons):
            ttk.Button(self.window, text=el, command=buttons[el]).grid(
                row=from_row + i, column=0, sticky="NESW", columnspan=columnspan)

    def clear_window(self):
        for el in self.window.winfo_children():
            el.destroy()


if __name__ == '__main__':
    program = Program("Among Us")
