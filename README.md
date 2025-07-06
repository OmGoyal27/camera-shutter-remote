# Camera Shutter Connector

A Python application that connects your camera shutter button to play an authentic shutter sound effect. This tool maps the Volume Up key to trigger a camera shutter sound, perfect for photography apps or camera simulators.

## Features

- 🔊 Plays authentic shutter sound when Volume Up key is pressed
- 🎮 Uses AutoHotkey for reliable hotkey detection
- 🎵 Includes built-in shutter sound effect
- ⚡ Lightweight and easy to use
- 🖥️ Windows compatible

## Requirements

- Python 3.6 or higher
- Windows operating system
- Audio output device

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Press the **Volume Up** key to trigger the shutter sound

3. Press **Enter** in the console to exit the application

## Files Description

- `main.py` - Main application script
- `shutter_sound.mp3` - Audio file containing the shutter sound effect
- `requirements.txt` - Python dependencies list
- `README.md` - This documentation file

## Dependencies

- **ahk[binary]** - AutoHotkey integration for Python
- **playsound** - Simple audio playback library

## How It Works

The application uses AutoHotkey (AHK) to monitor for the Volume Up key press. When detected, it plays the included shutter sound file using the playsound library. This creates a realistic camera shutter experience for photography applications or entertainment purposes.

## Customization

You can customize the application by:

- **Changing the hotkey**: Modify the `'Volume_Up'` parameter in `main.py` to use a different key
- **Using different sound**: Replace `shutter_sound.mp3` with your preferred audio file
- **Adding multiple sounds**: Extend the code to randomly select from multiple sound files

## Troubleshooting

- **No sound plays**: Check that your audio output is working and the volume is up
- **Hotkey not detected**: Ensure the application is running and has proper permissions
- **Import errors**: Make sure all dependencies are installed via `pip install -r requirements.txt`

## License

This project is open source under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.