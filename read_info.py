import requests
from datetime import datetime
from gtts import gTTS
import pygame
import os

# Function to get weather and air quality data
def get_weather_and_air_quality():
    weather_api_key = ''  # Your OpenWeatherMap API key
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q=Kochi,in&appid={weather_api_key}&units=metric'
    
    air_quality_url = ''  # Your AQICN token

    # Fetch weather data
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Fetch air quality data
    air_quality_response = requests.get(air_quality_url)
    air_quality_data = air_quality_response.json()

    if weather_response.status_code == 200:
        temp = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        wind_deg = weather_data['wind']['deg']
    else:
        temp, weather_desc, wind_speed, wind_deg = "unknown", "unknown", "unknown", "unknown"

    if air_quality_response.status_code == 200 and air_quality_data['status'] == 'ok':
        aqi = air_quality_data['data']['aqi']
    else:
        aqi = "unknown"

    return temp, weather_desc, wind_speed, wind_deg, aqi

# Function to read out time, date, weather, air quality, and wind info
def read_out_info():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%Y-%m-%d")

    temp, weather_desc, wind_speed, wind_deg, aqi = get_weather_and_air_quality()

    # Create text to read
    output_text = (f"The current time is {current_time}. "
                   f"Today's date is {current_date}. "
                   f"The temperature in Kochi is {temp} degrees Celsius with {weather_desc}. "
                   f"The wind speed is {wind_speed} meters per second. "
                   f"The air quality index is {aqi}.")

    # Generate audio using gTTS
    tts = gTTS(text=output_text, lang='en', tld='co.uk')
    tts_file = "output.mp3"
    tts.save(tts_file)

    # Initialize pygame and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(tts_file)
    pygame.mixer.music.set_volume(1.0)  # Set volume to 100%
    
    # Play the sound
    pygame.mixer.music.play()

    # Wait for the playback to finish
    while pygame.mixer.music.get_busy():  # Wait until the music is done playing
        pygame.time.Clock().tick(10)  # Check every 10 ms to avoid busy waiting

    # Stop the mixer
    pygame.mixer.music.stop()
    
    # Quit the mixer
    pygame.mixer.quit()

    # Clean up
    try:
        os.remove(tts_file)  # Delete the audio file
    except PermissionError:
        print(f"PermissionError: Could not delete {tts_file}. It may still be in use.")

# Run the function
if __name__ == "__main__":
    read_out_info()
