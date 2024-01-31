from st import stzb
from modules.web.web import ui
import threading

if __name__ == '__main__':
    try:
        new_thread = threading.Thread(target=ui.start)
        new_thread.setDaemon(True)
        new_thread.start()
        stzb.loop()
    except Exception as e:
        print(e)
