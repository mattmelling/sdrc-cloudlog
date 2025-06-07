import serial
from typing import Optional
from sdrc_cloudlog.background import BackgroundTask

MODES = ['', 'LSB', 'USB', 'CW', 'FM', 'AM']

class Rig(BackgroundTask):

    _port: Optional[serial.Serial] = None

    def send_command(self, cmd):
        self._port.write(f'{cmd};'.encode('ascii'))
        result = self._port.readline().decode().strip()
        return result

    def run(self) -> None:
        if not self._config.get('rig', 'enabled', False):
            return
        if self._port is None:
            self._port = serial.Serial(port=self._config.get('rig', 'port', 'COM1'),
                                       baudrate=self._config.get('rig', 'baud_rate', 57600),
                                       timeout=1)
        self._state.frequency = int(self.send_command('FA')[2:-1])
        self._state.mode = MODES[int(self.send_command('MD')[2:-1])]

    def end(self) -> None:
        if self._port is not None:
            self._port.close()
        self._port = None
