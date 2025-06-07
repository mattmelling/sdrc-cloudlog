import tkinter

from sdrc_cloudlog.ui.frame import SimpleEntryFrame
from sdrc_cloudlog.config import ConfigManager

class CloudlogFrame(SimpleEntryFrame):

    def __init__(self, master, config: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.add_switch(config.variable('cloudlog', 'enabled', False, tkinter.BooleanVar), 'Enable')
        self.add_entry(config.variable('cloudlog', 'radio', '', tkinter.StringVar), 'Radio Name')
        self.add_entry(config.variable('cloudlog', 'url', '', tkinter.StringVar), 'Cloudlog URL')
        self.add_entry(config.variable('cloudlog', 'key', '', tkinter.StringVar), 'Cloudlog API Key')
