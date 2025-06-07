import tkinter
import customtkinter

class EntryWithLabel(customtkinter.CTkFrame):
    def __init__(self, master, variable: tkinter.Variable, label: str, **kwargs):
        super().__init__(master, fg_color='transparent', **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self._label = customtkinter.CTkLabel(self, text=label)
        self._label.grid(row=0, column=1, pady=(2, 1), sticky='w')

        self._entry = customtkinter.CTkEntry(self, textvariable=variable, width=250, height=32, placeholder_text=label)
        self._entry.grid(row=1, column=1, pady=(1, 2), sticky='w')
