# Read-Aloud Weather Report Script

This Python script provides a spoken weather report, including the current time, date, weather conditions, wind information, and Air Quality Index (AQI).

## Features
- Retrieves real-time weather and AQI data via APIs.
- Reads information aloud using gTTS (Google Text-to-Speech).
- Uses **pygame** for audio playback.
- Deletes the audio file after use to save space.
- Handles missing data by stating "unknown."

## Requirements
- Python 3.x
- **pygame** for audio playback
- **gTTS** for speech synthesis
- An internet connection for API requests
- 
##Notes
 - API keys must be configured in the script (Use your own API Keys). Instructions for setting them up are provided in the code.
 - Ensure pygame is installed for proper audio functionality.
 - The audio file will be deleted after playback to avoid cluttering your system.
