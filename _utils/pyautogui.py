import pyautogui

def press(key):
    pyautogui.press(key)

def hotkey(keys):
    pyautogui.hotkey(*keys)

def moveTo(coordinate):
    pyautogui.moveTo(*coordinate)

def click(coordinate = []):
    if len(coordinate) > 0:
        pyautogui.click(*coordinate)
    else:
        pyautogui.click()

def display_mouse_position():
    pyautogui.displayMousePosition()