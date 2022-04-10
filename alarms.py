import time
from datetime import datetime

from playsound import playsound
from settings import Settings


def play_kuku_sound():
    """Play the kuku sound once."""
    settings = Settings()
    time.sleep(0.5)
    playsound(settings.kuku_sound)


def minutely_alarms():
    """Make kukuk sound every 5 seconds, for testing purposes."""
    alarms = ["00", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
    current_time = datetime.now().strftime("%S")

    if current_time in alarms:
        play_kuku_sound()
        

def quarterly_alarms():
    """Make kukuk sound every 15 minutes."""
    alarms = ["15:00", "30:00", "45:00"]
    current_time = datetime.now().strftime("%M:%S")

    if current_time in alarms:
        play_kuku_sound()

def hourly_alarms():
    """Make kukuk sound according to the hours."""
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == "00:00:00" or current_time == "12:00:00":
        play_kuku_sound() * 12
    if current_time == "01:00:00" or current_time == "13:00:00":
        play_kuku_sound() * 1
    if current_time == "02:00:00" or current_time == "14:00:00":
        play_kuku_sound() * 2
    if current_time == "03:00:00" or current_time == "15:00:00":
        play_kuku_sound() * 3
    if current_time == "04:00:00" or current_time == "16:00:00":
        play_kuku_sound() * 4
    if current_time == "05:00:00" or current_time == "17:00:00":
        play_kuku_sound() * 5
    if current_time == "06:00:00" or current_time == "18:00:00":
        play_kuku_sound() * 6
    if current_time == "07:00:00" or current_time == "19:00:00":
        play_kuku_sound() * 7
    if current_time == "08:00:00" or current_time == "20:00:00":
        play_kuku_sound() * 8
    if current_time == "09:00:00" or current_time == "21:00:00":
        play_kuku_sound() * 9
    if current_time == "10:00:00" or current_time == "22:00:00":
        play_kuku_sound() * 10
    if current_time == "11:00:00" or current_time == "23:00:00":
        play_kuku_sound() * 11
