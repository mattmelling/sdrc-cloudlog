import tkinter
from typing import Dict, Any, Type

class State:
    _variables: Dict[str, tkinter.Variable]

    def __init__(self) -> None:
        self._variables = {}

    def variable(self, name: str, default: Any, var_type: Type[tkinter.Variable]) -> tkinter.Variable:
        if name not in self._variables:
            self._variables[name] = var_type(value=default)
        return self._variables[name]

    @property
    def frequency_var(self) -> tkinter.Variable:
        return self.variable('frequency', 0, tkinter.IntVar)

    @property
    def frequency(self) -> int:
        return self.frequency_var.get()

    @frequency.setter
    def frequency(self, value: int) -> None:
        self.frequency_var.set(value)

    @property
    def mode_var(self) -> tkinter.Variable:
        return self.variable('mode', 'USB', tkinter.StringVar)

    @property
    def mode(self) -> str:
        return self.mode_var.get()

    @mode.setter
    def mode(self, value) -> None:
        self.mode_var.set(value)
