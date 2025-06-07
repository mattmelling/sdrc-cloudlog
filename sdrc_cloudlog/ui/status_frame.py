import tkinter
import customtkinter

from sdrc_cloudlog.state import State
from sdrc_cloudlog.config import ConfigManager

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, master, config: ConfigManager, state: State, **kwargs):
        super().__init__(master, **kwargs)

        self._state = state
        self._config = config
        self._freq_pretty_var = tkinter.StringVar()
        self._tx_freq_pretty_var = tkinter.StringVar()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        state.frequency_var.trace_add('write', self.update_freq_pretty)
        state.frequency_var.trace_add('write', self.update_tx_freq_pretty)

        self._freq_label = customtkinter.CTkLabel(self, text='No connection', font=('monospace', 36), anchor='center', textvariable=self._freq_pretty_var)
        self._freq_label.grid(row=0, column=0, columnspan=3, sticky='ew')

        self._mode_label = customtkinter.CTkLabel(self, text='USB', font=('monospace', 12), textvariable=self._state.mode_var)
        self._mode_label.grid(row=1, column=0, sticky='w')

        self._tx_offset_label = customtkinter.CTkLabel(self, text='TX', font=('monospace', 12), anchor='center', textvariable=self._tx_freq_pretty_var)
        self._tx_offset_label.grid(row=1, column=1, sticky='e')

        prop_mode_var = self._config.variable('defaults', 'prop_mode', '', tkinter.StringVar)
        self._status_label = customtkinter.CTkLabel(self, font=('monospace', 12), textvariable=prop_mode_var)
        self._status_label.grid(row=1, column=2, sticky='e')

    def format_frequency(self, f: int) -> str:
        return '{:,}'.format(f).replace(',', '.')

    def update_freq_pretty(self, var, index, mode):
        self._freq_pretty_var.set(self.format_frequency(self._state.frequency))

    def update_tx_freq_pretty(self, var, index, mode):
        f = self._state.frequency + self._config.get('rig', 'tx_offset', 0)
        print(self._config.get('rig', 'tx_offset', 0))
        self._tx_freq_pretty_var.set(f'TX={self.format_frequency(f)}')
