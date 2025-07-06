import ahk as autohotkey

def shutter_button_pressed():
    print("Shutter button pressed!")

ahk = autohotkey.AHK()
ahk.add_hotkey('Volume_Up', shutter_button_pressed)
ahk.start_hotkeys()

input("Press Enter to exit...\n")
ahk.stop_hotkeys()