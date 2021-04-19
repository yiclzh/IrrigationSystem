from time import sleep
from rq import get_current_job

import os

IS_ON_PI = os.getenv('IS_ON_PI', False)

if IS_ON_PI:
    import RPi.GPIO as GPIO

def turning_on() :
    if IS_ON_PI:
        GPIO.setmode( GPIO.BCM )
        GPIO.setwarnings = (False)

    station1 = 18
    station2 = 24
    station3 = 26
    station4 = 6
    station5 = 17

    if IS_ON_PI :
        GPIO.setup( station1, GPIO.OUT )
        GPIO.setup( station2, GPIO.OUT )
        GPIO.setup( station3, GPIO.OUT )
        GPIO.setup( station4, GPIO.OUT )
        GPIO.setup( station5, GPIO.OUT )

    sleep_time = 6

    job = get_current_job()
    job.meta['progress'] = 0
    job.save_meta()

    # start station 1
    if IS_ON_PI :
        job.refresh()
        if job.meta.__contains__("canceled") and job.meta['canceled']:
            return

        GPIO.output( station1, 1 )

    sleep(sleep_time)

    if IS_ON_PI :
        GPIO.output( station1, 0 )
    # station 1 is done
    print('Station 1 is done')
    job.meta['progress'] = 20
    job.save_meta()
    sleep(5)
    #Start Station 2
    if IS_ON_PI :
        job.refresh()
        if job.meta.__contains__("canceled") and job.meta['canceled']:
            return
        GPIO.output( station2, 1 )
    sleep( sleep_time )
    if IS_ON_PI :
        GPIO.output( station2, 0 )
    #Station 2 is done
    print('Station 2 is done')
    job.meta['progress'] = 40
    job.save_meta()
    sleep(5)
    #Start Station 3
    if IS_ON_PI :
        job.refresh()
        if job.meta.__contains__("canceled") and job.meta['canceled']:
            return
        GPIO.output( station3, 1)
    sleep( sleep_time )
    if IS_ON_PI :
        GPIO.output( station3, 0 )
    # Station 3 is done
    print('Station 3 is done')
    job.meta['progress'] = 60
    job.save_meta()
    sleep(5)
    #Start Station 4
    if IS_ON_PI :
        job.refresh()
        if job.meta.__contains__("canceled") and job.meta['canceled']:
            return
        GPIO.output( station4, 1 )
    sleep( sleep_time )
    if IS_ON_PI :
        GPIO.output( station4, 0 )
    #Station 4 is done
    print('Station 4 is done')
    job.meta['progress'] = 80
    job.save_meta()
    sleep(5)
    #Start Station 5
    if IS_ON_PI :
        job.refresh()
        if job.meta.__contains__("canceled") and job.meta['canceled']:
            return
        GPIO.output( station5, 1 )
    sleep( sleep_time )
    if IS_ON_PI :
        GPIO.output( station5, 0 )
    #Station 5 is done
    print('Station 5 is done')
    job.meta['progress'] = 100
    job.save_meta()
    print('Irrigation is done')




