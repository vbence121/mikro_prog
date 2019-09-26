import RPi.GPIO as GPIO
import sleep
import time

GPIO.setmode(GPIO.BCM)

from api_keys import *

GPIO_Trigger = 18
GPIO_Echo = 24
GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setupt(GPIO_Echo, GPIO.IN)

def check_dist ():
    GPIO.output(GPIO_Trigger, GPIO.HIGH) # set trigger to high
    sleep(1/1000)
    GPIO.output(GPIO_Trigger, GPIO.LOW)

    StartTime = time() # set start and arrive time
    ArriveTime = time()

    while GPIO.input(GPIO_Echo) == 0:
        StartTime = time()

    while GPIO.input(GPIO_Echo) == 1:
        ArriveTime = time()

    dif = ArriveTime - StartTime
    # t*sonic_speed/2 = distance
    dist = (dif * 34300) / 2

    return dist

static_distance = 1000
def check_presence ( dist ):
    if ( dist < static_distance ):
        return False
    else:
        return True

def blink ( pin ):
    GPIO.output(pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin, GPIO.LOW)
    sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin, GPIO.HIGH)
    sleep(4)
    GPIO.output(pin, GPIO.LOW)
    return

gatePin=18
ledGPin=18
ledRPin=18

import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

"""import telegram
tele_bot = telegram.Bot(token=TELE_TOKEN)
"""

timer_amount = 60
j=timer_amount

numberOfSpaces = 100
emptySpaces=numberOfSpaces

dist_sens= True

while True:
    if : # if rfid detected
    if emptySpaces < numberOfSpaces: # there is space
    if 0: # in datasheet
        GPIO.output(ledGPin, GPIO.HIGH) # turn on green led
        GPIO.output(gatePin, GPIO.HIGH) # trigger gate pin
        while dist_sens  j < timer_amount:  # start enterance timer
            dist_sens = check_presence(check_dist)
            j++
        dist_sens = check_presence(check_dist() #check object presence
        while dist_sens: # if timer ended but object is still present
            sleep( 5 )
            dist_sens = check_presence( check_dist() ) # check presence
        emptySpaces-- #  adjust nmbr of spaces
        GPIO.output(ledGPin, GPIO.LOW) # turn off green led
        GPIO.output(gatePin, GPIO.LOW)  # close gate
        pi.update_status(emptySpaces) # send out msg to outer serv
    else # turn on red led
        blink(ledRPin)
except KeyboardInterupt:
    GPIO.cleanup()
