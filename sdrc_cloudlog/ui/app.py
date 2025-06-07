import customtkinter

from sdrc_cloudlog.config import ConfigManager
from sdrc_cloudlog.state import State

from .status_frame import StatusFrame
from .rig_frame import RigFrame
from .cloudlog_frame import CloudlogFrame
from .defaults_frame import DefaultsFrame

class App(customtkinter.CTk):
    def __init__(self, config: ConfigManager, state: State):
        super().__init__()

        self.grid_columnconfigure(0, weight=1)

        self._tabs = customtkinter.CTkTabview(self, width=400, height=200, state='normal')
        self._tabs.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        tab_status = self._tabs.add('Status')
        tab_status.grid_columnconfigure(0, weight=1)
        self._status = StatusFrame(tab_status, config, state)
        self._status.grid(row=0, column=0, padx=20, pady=20)

        tab_defaults = self._tabs.add('Defaults')
        tab_defaults.grid_columnconfigure(0, weight=1)
        self._defaults = DefaultsFrame(tab_defaults, config)
        self._defaults.grid(row=0, column=0, padx=20, pady=20)

        tab_settings = self._tabs.add('Cloudlog')
        tab_settings.grid_columnconfigure(0, weight=1)
        self._settings = CloudlogFrame(tab_settings, config)
        self._settings.grid(row=0, column=0, padx=20, pady=20)

        tab_rig = self._tabs.add('Rig')
        tab_rig.grid_columnconfigure(0, weight=1)
        self._rig = RigFrame(tab_rig, config)
        self._rig.grid(row=0, column=0, padx=20, pady=20)
