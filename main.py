#-*- coding: utf-8 -*-
#qpy:kivy


import traceback
import os

from program import VKBotApp
from bot.utils import PATH
from bot.utils import DATA_PATH

def main():
    try:
        if not os.path.exists(PATH) and PATH:
            os.makedirs(PATH)
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        VKBotApp().run()
    except Exception:
        error_text = traceback.format_exc()
        open(PATH + 'error.log', 'w').write(error_text)

if __name__ == '__main__':
    main()
