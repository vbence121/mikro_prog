import RPi.GPIO as GPIO
import sleep
import time

gatePin=18
ledGPin=18
ledRPin=18

import twitter
api = twitter.Api(consumer_key=[consumer key],
                  consumer_secret=[consumer secret],
                  access_token_key=[access token],
                  access_token_secret=[access token secret])

numberOfSpaces=100
emptySpaces=numberOfSpaces

while True:
    #if rfid detected
    # if in datasheet
    #   turn on led
        """GPIO.output(ledGPin, GPIO.HIGH)"""
    #   open gate && start enterance timer
        """GPIO.output(gatePin, GPIO.HIGH)"""
    #   adjust nmbr of spaces
        """emptySpaces--"""
    #     send out msg to outer serv
          """twitter.api.API.PostUpdate()"""
    # else turn on wrong red
        """GPIO.output(ledRPin, GPIO.HIGH)"""
