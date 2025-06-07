import tkinter
import customtkinter

from .entry import EntryWithLabel
from sdrc_cloudlog.config import ConfigManager

class DefaultsFrame(customtkinter.CTkFrame):
    def __init__(self, master, config: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        def_pwr_var = config.variable('defaults', 'power', 1, tkinter.DoubleVar)
        self._def_pwr_entry = EntryWithLabel(self, def_pwr_var, 'Power (W)')
        self._def_pwr_entry.grid(row=0, column=1)

        def_sat_var = config.variable('defaults', 'sat_name', '', tkinter.StringVar)
        self._def_sat_entry = EntryWithLabel(self, def_sat_var, 'Satellite Name')
        self._def_sat_entry.grid(row=1, column=1)

        def_prop_var = config.variable('defaults', 'prop_mode', '', tkinter.StringVar)
        self._def_prop_entry = EntryWithLabel(self, def_prop_var, 'Propagation Mode')
        self._def_prop_entry.grid(row=2, column=1)
