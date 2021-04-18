from time import sleep
from rq import get_current_job

import os

IS_ON_PI = os.getenv('IS_ON_PI', False)

if IS_ON_PI:
    import RPi.GPIO as GPIO

if IS_ON_PI:
    import RPi.GPIO as GPIO

def turning_off() :
    if IS_ON_PI:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings = (False)

    station1 = 18
    station2 = 24
    station3 = 26
    station4 = 6
    station5 = 17

    if IS_ON_PI:
        GPIO.setup( station1, GPIO.OUT)
        GPIO.setup( station2, GPIO.OUT )
        GPIO.setup( station3, GPIO.OUT )
        GPIO.setup( station4, GPIO.OUT )
        GPIO.setup( station5, GPIO.OUT )

    job = get_current_job()
    job.meta['progress'] = 0
    job.save_meta()

    if IS_ON_PI:
        GPIO.output(station1, 0)
    print("Turned off station1")
    job.meta['progress'] = 20
    job.save_meta()

    if IS_ON_PI:
        GPIO.output(station2, 0)
    print("Turned off station2")
    job.meta['progress'] = 40
    job.save_meta()
    if IS_ON_PI:
        GPIO.output(station3, 0)
    print("Turned off station3")
    job.meta['progress'] = 60
    job.save_meta()
    if IS_ON_PI:
        GPIO.output(station4, 0)
    print("Turned off station4")
    job.meta['progress'] = 80
    job.save_meta()
    if IS_ON_PI:
        GPIO.output(station5, 0)
    print("Turned off station5")
    job.meta['progress'] = 100
    job.save_meta()
    print("Irrigation has been turned off")
