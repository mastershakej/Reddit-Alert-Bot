from utils.color import Color
import traceback
from random import randint

class Logger:

    @staticmethod
    def log(string):
        try:
            print(string)
        except:
            print(traceback.format_exc())

    @staticmethod
    def aligntext(text, desired_spaces):
        additional_space = desired_spaces - len(text)
        while additional_space > 0:
            text += ' '
            additional_space -= 1
        return text
