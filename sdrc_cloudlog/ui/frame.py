import tkinter
import customtkinter
from sdrc_cloudlog.ui.entry import EntryWithLabel

class SimpleEntryFrame(customtkinter.CTkFrame):

    _row: int = 10

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

    def add_entry(self, variable: tkinter.Variable, label: str):
        f = EntryWithLabel(self, variable, label)
        f.grid(row=self._row, column=1)
        self._row += 1

    def add_switch(self, variable: tkinter.Variable, label: str):
        f = customtkinter.CTkSwitch(self, text=label, variable=variable, onvalue=True, offvalue=False)
        f.grid(row=self._row, column=1, sticky='w')
        self._row += 1
