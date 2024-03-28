from modules.web.config import WebConfig
def start():
  config = WebConfig()
  print(config.get_main_data())

if __name__ == '__main__':
  start()
