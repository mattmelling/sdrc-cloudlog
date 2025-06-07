from .ui.app import App
from .config import ConfigManager
from .state import State
from .rig import Rig
from .cloudlog import Cloudlog


def main():
    config = ConfigManager()
    state = State()

    app = App(config, state)

    rig = Rig(config, state, interval=0.5)
    rig.start()

    cloudlog = Cloudlog(config, state, interval=1)
    cloudlog.start()

    app.mainloop()
    rig.stop()
    cloudlog.stop()


if __name__ == '__main__':
    main()
