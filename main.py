import ahk as autohotkey
import pyautogui as pg
import playsound

def shutter_button_pressed():
    pg.hotkey('win', 'd')

ahk = autohotkey.AHK()
ahk.add_hotkey('Volume_Up', shutter_button_pressed)
ahk.start_hotkeys()

input("Press Enter to exit...\n")
ahk.stop_hotkeys()