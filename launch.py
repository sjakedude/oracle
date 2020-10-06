import RPi.GPIO as GPIO
from time import sleep
import random
from pygame import mixer

mixer.init()
mixer.music.load('/home/pi/Desktop/song.mp3')
mixer.music.play()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(40, GPIO.OUT, initial=GPIO.HIGH)

def flashing():
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    sleep(.2)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
    sleep(.2)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    sleep(.2)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
    sleep(.2)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    sleep(.2)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
    sleep(.2)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    sleep(.2)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
    sleep(.2)
    GPIO.output(38, GPIO.HIGH)
    GPIO.output(40, GPIO.HIGH)
    sleep(.2)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(40, GPIO.LOW)
    sleep(.2)

def displayAnswer(num):
    if num is 0:
        mixer.Channel(1).play(mixer.Sound('/home/pi/Desktop/Noooo.wav'))
        GPIO.output(40, GPIO.HIGH)
    else:
        mixer.Channel(0).play(mixer.Sound('/home/pi/Desktop/Yeah.wav'))
        GPIO.output(38, GPIO.HIGH)

def calculate():
    num = random.randint(0, 1)
    flashing()
    displayAnswer(num)

while True:
    try:
        GPIO.output(8, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        if GPIO.input(10) == GPIO.HIGH:
            mixer.music.pause()
            GPIO.output(8, GPIO.LOW)
            sleep(1)
            mixer.Channel(0).play(mixer.Sound('/home/pi/Desktop/Uhhhh.wav'))
            calculate()
            sleep(5)
            mixer.music.unpause()
    finally:
        GPIO.output(8, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)


