# from st import stzb
from modules.web.web import ui

if __name__ == '__main__':
    try:
        ui.start()
        # new_thread = threading.Thread(target=ui.start)
        # new_thread.setDaemon(True)
        # new_thread.start()
        # register_thread(threading.current_thread())
        # stzb.loop()
    except Exception as e:
        print(e)