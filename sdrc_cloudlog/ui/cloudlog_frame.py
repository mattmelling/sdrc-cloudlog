import tkinter
import customtkinter

from .entry import EntryWithLabel
from sdrc_cloudlog.config import ConfigManager

class CloudlogFrame(customtkinter.CTkFrame):

    def __init__(self, master, config: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        cl_enable_switch_var = config.variable('cloudlog', 'enabled', False, tkinter.BooleanVar)
        self._cl_enable_switch = customtkinter.CTkSwitch(self, text='Enable', variable=cl_enable_switch_var, onvalue=True, offvalue=False)
        self._cl_enable_switch.grid(row=0, column=1, sticky='w')

        cl_radio_var = config.variable('cloudlog', 'radio', '', tkinter.StringVar)
        self._cl_radio_entry = EntryWithLabel(self, cl_radio_var, 'Radio Name')
        self._cl_radio_entry.grid(row=1, column=1)

        cl_url_var = config.variable('cloudlog', 'url', '', tkinter.StringVar)
        self._cl_url_entry = EntryWithLabel(self, cl_url_var, 'Cloudlog URL')
        self._cl_url_entry.grid(row=2, column=1)

        cl_key_var = config.variable('cloudlog', 'key', '', tkinter.StringVar)
        self._cl_key_entry = EntryWithLabel(self, cl_key_var, 'Cloudlog API Key')
        self._cl_key_entry.grid(row=3, column=1)
