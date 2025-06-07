import requests
from datetime import datetime
from sdrc_cloudlog.background import BackgroundTask

class Cloudlog(BackgroundTask):

    def run(self) -> None:
        if not self._config.get('cloudlog', 'enabled', False):
            return

        cl_url = self._config.get('cloudlog', 'url', '')
        tx_off = self._config.get('rig', 'tx_offset', 0)
        payload = {
            'key': self._config.get('cloudlog', 'key', ''),
            'radio': self._config.get('cloudlog', 'radio', ''),
            'frequency': self._state.frequency + tx_off,
            'frequency_rx': self._state.frequency,
            'power': self._config.get('defaults', 'power', ''),
            'satname': self._config.get('defaults', 'sat_name', ''),
            'timestamp': datetime.now().strftime('%Y/%m/%d %H:%M'),
            'mode': self._state.mode,
            'prop_mode': self._config.get('defaults', 'prop_mode', ''),
            'sat_name': self._config.get('defaults', 'sat_name', '')
        }
        requests.post(f'{cl_url}/api/radio', json=payload)
