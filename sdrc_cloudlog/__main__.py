from sdrc_cloudlog.ui.app import App
from sdrc_cloudlog.config import ConfigManager
from sdrc_cloudlog.state import State
from sdrc_cloudlog.rig import Rig
from sdrc_cloudlog.cloudlog import Cloudlog


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
