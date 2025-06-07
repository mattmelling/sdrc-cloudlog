import tkinter
import customtkinter

from .entry import EntryWithLabel
from sdrc_cloudlog.config import ConfigManager

class RigFrame(customtkinter.CTkFrame):
    def __init__(self, master, config: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        rig_enbl_var = config.variable('rig', 'enabled', False  , tkinter.BooleanVar)
        self._rig_enbl_switch = customtkinter.CTkSwitch(self, text='Enable', variable=rig_enbl_var, onvalue=True, offvalue=False)
        self._rig_enbl_switch.grid(row=0, column=1, sticky='w')

        rig_port_var = config.variable('rig', 'port', 'COM1', tkinter.StringVar)
        self._rig_port_entry = EntryWithLabel(self, rig_port_var, 'Rig Port')
        self._rig_port_entry.grid(row=1, column=1)

        rig_baud_var = config.variable('rig', 'baud', 57600, tkinter.IntVar)
        self._rig_baud_entry = EntryWithLabel(self, rig_baud_var, 'Baud Rate')
        self._rig_baud_entry.grid(row=2, column=1)

        rig_tx_offset_var = config.variable('rig', 'tx_offset', 0, tkinter.IntVar)
        self._rig_tx_offset_entry = EntryWithLabel(self, rig_tx_offset_var, 'TX Offset')
        self._rig_tx_offset_entry.grid(row=3, column=1)
