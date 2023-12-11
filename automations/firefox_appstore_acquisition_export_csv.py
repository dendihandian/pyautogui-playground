import sys
import os
sys.path.append(os.getcwd())

from _utils.pyautogui import click, moveTo, press
from time import sleep

def handler():

    sleep(15)

    for i in range(100):
        moveTo([1808, 300])
        sleep(1)
        click()
        sleep(1)
        moveTo([1817,607])
        sleep(1)
        click()
        sleep(1)
        press('esc')
        sleep(1)


if __name__ == '__main__':
    handler()