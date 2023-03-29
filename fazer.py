import board
import digitalio
import time
import analogio
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile
# Set up the light sensor
light_sensor_pin = board.LIGHT
light_sensor = analogio.AnalogIn(light_sensor_pin)

# Set up the speaker
speaker = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker.direction = digitalio.Direction.OUTPUT
speaker.value = True
audio = AudioOut(board.SPEAKER)
path = "sounds/"
# Set up the threshold for light level
threshold = 20000
def play_sound(filename):
    with open(path + filename, "rb") as wave_file:
        wave = WaveFile(wave_file)
        audio.play(wave)
        while audio.playing:
            pass

# Loop forever
while True:
    # Read the value of the light sensor
    light_value = light_sensor.value

    # If the light level exceeds the threshold, play a sound
    if light_value > threshold:
        play_sound("yo.wav")

    # Wait for a moment before looping again
    time.sleep(0.2)
