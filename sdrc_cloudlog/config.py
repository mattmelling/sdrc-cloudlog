import tkinter
import toml
import os
from platformdirs import user_config_dir

from typing import Any, Dict, Type

CONFIG_FILENAME = os.path.join(user_config_dir('sdrc-console', 'G4IYT'), 'config.toml')

class ConfigManager:

    _variables: Dict[str, Dict[str, tkinter.Variable]]

    def __init__(self) -> None:
        if not os.path.exists(CONFIG_FILENAME):
            os.makedirs(os.path.dirname(CONFIG_FILENAME), exist_ok=True)
            open(CONFIG_FILENAME, 'w').close()
        self._variables = {}
        with open(CONFIG_FILENAME, 'r') as f:
            self._config = toml.load(f)

    def get(self, parent: str, name: str, default: Any) -> Any:
        return self._config.get(parent, {}).get(name, default)

    def set(self, parent: str, name: str, value: Any) -> None:
        if parent not in self._config:
            self._config[parent] = {}
        self._config[parent][name] = value

        with open(CONFIG_FILENAME, 'w') as f:
            toml.dump(self._config, f)

    def variable(self, parent: str, name: str, default: Any, var_type: Type[tkinter.Variable]) -> tkinter.Variable:
        if parent not in self._variables:
            self._variables[parent] = {}
        if name not in self._variables[parent]:
            variable = var_type(value=self.get(parent, name, default))
            variable.trace_add('write', lambda var_name, index, mode: self.set(parent, name, variable.get()))
            self._variables[parent][name] = variable
        return self._variables[parent][name]
