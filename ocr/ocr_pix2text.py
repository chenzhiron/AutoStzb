from pix2text import Pix2Text
from config.paths import path

if __name__ == '__main__':
    p2t = Pix2Text(analyzer_config=dict(model_name='mfd'))
    outs = p2t.recognize(path, resized_shape=960, use_analyzer=False)
    print(outs)
