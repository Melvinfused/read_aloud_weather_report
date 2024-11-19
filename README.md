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

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
##Notes
 - API keys must be configured in the script. Instructions for setting them up are provided in the code.
 - Ensure pygame is installed for proper audio functionality.
 - The audio file will be deleted after playback to avoid cluttering your system.
