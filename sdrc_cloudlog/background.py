import threading
import time

from abc import abstractmethod
from sdrc_cloudlog.config import ConfigManager
from sdrc_cloudlog.state import State

class BackgroundTask:
    """
    A background task that runs at regular intervals
    """

    _stop: bool = False

    def __init__(self, config: ConfigManager, state: State, interval: float = 1) -> None:
        self._config = config
        self._state = state
        self._interval = interval

    def start(self) -> threading.Thread:
        t = threading.Thread(target=self.loop)
        t.start()
        return t

    def loop(self) -> None:
        while not self._stop:
            self.run()
            time.sleep(self._interval)

    def stop(self) -> None:
        self._stop = True
        self.end()

    @abstractmethod
    def run(self) -> None:
        pass

    def end(self) -> None:
        pass
