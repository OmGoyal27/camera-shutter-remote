import ahk as autohotkey
import playsound

def shutter_button_pressed():
    playsound.playsound('shutter_sound.mp3')

ahk = autohotkey.AHK()
ahk.add_hotkey('Volume_Up', shutter_button_pressed)
ahk.start_hotkeys()

input("Press Enter to exit...\n")
ahk.stop_hotkeys()