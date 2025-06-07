import tkinter

from sdrc_cloudlog.config import ConfigManager
from sdrc_cloudlog.ui.frame import SimpleEntryFrame

class RigFrame(SimpleEntryFrame):
    def __init__(self, master, config: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.add_switch(config.variable('rig', 'enabled', False  , tkinter.BooleanVar), 'Enable')
        self.add_entry(config.variable('rig', 'port', 'COM1', tkinter.StringVar), 'Rig Port')
        self.add_entry(config.variable('rig', 'baud', 57600, tkinter.IntVar), 'Baud Rate')
        self.add_entry(config.variable('rig', 'tx_offset', 0, tkinter.IntVar), 'TX Offset')
