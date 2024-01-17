import threading
from st import stzb
from modules.web.web import start_web

if __name__ == '__main__':
    new_thread = threading.Thread(target=start_web)
    new_thread.setDaemon(True)
    new_thread.start()
    stzb.loop()