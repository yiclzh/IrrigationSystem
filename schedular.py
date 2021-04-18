
from crontab import CronTab

COMMENT_ID = 'abc234345'

username = "yiruclare"

class ScheduleJob:
    def __init__(self, minute, hour, day, dow, months, enabled):
        self.minute = minute
        self.hour = hour
        self.day = day
        self.dow = dow
        self.months = months
        self.enabled = enabled

    def __str__(self):
        s = f"minute: {self.minute}, hour: {self.hour}, "
        s = s + f"day: {self.day}, dow: {self.dow}, months: {self.months}"
        return s

def update_schedule(minute, hour, day, dow, months):
    job = None
    cron = CronTab(user= username)
    for p in cron.find_comment(COMMENT_ID):
        job = p

    if job == None:
        print("Job not found")
    else:
        job.minute.on()
        job.minute.on(minute)
        job.hour.on()
        job.hour.on(hour)
        job.day.on()
        job.day.on(day)
        job.dow.on()
        job.dow.parse(dow)
        job.months.on()
        job.montha.parse(months)
        cron.write()

def add() :
    cron = CronTab( user= username )
    job = cron.new( command='irrigation_on.py', comment=COMMENT_ID )
    cron.write()

def subtract():
    cron = CronTab(user= username)
    job = cron.new(command='irrigation_off.py', comment=COMMENT_ID)
    job.enable(False)
    cron.write()

def get_current():
    job = None
    cron = CronTab(user= username)
    for p in cron.find_comment(COMMENT_ID):
        job = p

    if job == None:
        return None
    else:
        return ScheduleJob(job.minute.__str__(),
                           job.hour.__str__(),
                           job.day.__str__(),
                           job.dow.__str__(),
                           job.months.__str__(),
                           job.enabled)

def print_current():
    job = None
    cron = CronTab(user= username)
    for p in cron.find_comment(COMMENT_ID):
        job = p

    if job == None:
        print("Job not found")
    else:
        print("Job found, scheduled on:")
        print(f"\tmonth: {job.month.__str__()}")
        print(f"\tday: {job.day.__str__()}")
        print(f"\tday of week: {job.dow.__str__()}")
        print(f"\thour: {job.hour.__str__()}")
        print(f"\tminute: {job.minute.__str__()}")

def disable_job():
    job = None
    cron = CronTab(user= username)
    for p in cron.find_comment(COMMENT_ID):
        job = p

    if job == None:
        print("Job not found")
    else:
        job.enable(False)
        cron.write()

def enable_job():
    job = None
    cron = CronTab(user= username )
    for p in cron.find_comment(COMMENT_ID):
        job = p
    if job == None:
        print("Job not found")
    else:
        job.enable()
        cron.write()

def check_job():
    job = None
    cron = CronTab(user= username )
    for p in cron.find_comment(COMMENT_ID):
        job = p
    if job == None:
        print("Job not found")
    else:
        job.is_enabled()
        cron.write()

def check_job_valid():
    job = None
    cron = CronTab( user= username )
    for p in cron.find_comment( COMMENT_ID ) :
        job = p
    if job == None :
        print( "Job not found" )
    else :
        job.is_valid()
        cron.write()


def get_edit_schedule_records(_minutes, _hour, _day, _dow, _months, ):
    job = None
    cron = CronTab( user= username )
    for p in cron.find_comment( COMMENT_ID ) :
        job = p

    if _day=="":
        job.day.on()
        job.day.parse('*')
    else:
        job.day.on()
        job.day.parse(_day)

    if _dow=="":
        job.dow.on()
        job.dow.parse('*')

    else:
        job.dow.on()
        job.dow.parse(_dow)

    if _months=="":
        job.months.on()
        job.months.parse('*')
    else:
        job.months.on()
        job.months.parse( _months )


    job.minute.on()
    job.minute.on(_minutes)
    job.hour.on()
    job.hour.on(_hour)
    cron.write()


if __name__ == '__main__':
    app.run(debug=True)













