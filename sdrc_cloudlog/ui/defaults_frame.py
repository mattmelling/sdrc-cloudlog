import tkinter

from sdrc_cloudlog.config import ConfigManager
from sdrc_cloudlog.ui.frame import SimpleEntryFrame

class DefaultsFrame(SimpleEntryFrame):
    def __init__(self, master, config: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.add_entry(config.variable('defaults', 'power', 1, tkinter.DoubleVar), 'Power (W)')
        self.add_entry(config.variable('defaults', 'sat_name', '', tkinter.StringVar), 'Satellite Name')
        self.add_entry(config.variable('defaults', 'prop_mode', '', tkinter.StringVar), 'Propagation Mode')
