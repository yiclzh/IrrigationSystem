from flask import Flask, render_template, request
import json
from redis import Redis
import rq

app = Flask(__name__)

from . import schedular

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/schedule')
def schedule():
    s = schedular.get_current()
    print (s)
    return render_template('schedule.html', schedule = s)

@app.route('/edit_schedule')
def edit_schedule():
    s = schedular.get_current()
    print (s)
    return render_template('edit_schedule.html', schedule=s)

@app.route("/get-compare-data", methods=['POST'])
def get_compare_data():
    request_json_obj = request.get_json()
    print(json.dumps(request_json_obj, indent=2))

    _minutes = request_json_obj['minutes']
    _hour = request_json_obj['hour']
    _day = request_json_obj['day']
    _dow = request_json_obj['dow']
    _months = request_json_obj['months']


    schedular.get_edit_schedule_records(_minutes=_minutes,
                                                                 _hour=_hour,
                                                                 _day=_day,
                                                                 _dow=_dow,
                                                                 _months=_months)

    return 'OK'


@app.route("/btn-disable-schedule", methods=['POST'])
def get_disable_schedule():
    schedular.disable_job()

    return 'OK'

@app.route("/btn-enable-schedule", methods=['POST'])
def get_enable_schedule():
    schedular.enable_job()

    return 'OK'
   
@app.route("/irrigation-on", methods=['POST'])
def irrigation_on():
    redis = Redis.from_url('redis://')
    job_id = "irrigationid"
    queue = rq.Queue('irrigation-tasks', connection=redis)
    job = queue.fetch_job(job_id)
    if job is None or job.is_finished:
        print(job)
        queue.enqueue('irrigation_on.turning_on', job_id = job_id,
                        job_timeout = "1h")
        return 'STARTED'
    else:
        print(job)
        return 'ALREADLY RUNNING'

@app.route("/irrigation-off", methods=['POST'])
def irrigation_off():
    redis = Redis.from_url('redis://')
    job_id = "irrigationid"
    queue = rq.Queue('irrigation-tasks', connection=redis)
    job = queue.fetch_job(job_id)
    if job is None:
        queue.enqueue('irrigation_off.turning_off', job_id=job_id, )
        return 'NO JOB IS RUNNING'
    else:

        queue.enqueue('irrigation_off.turning_off', job_id=job_id, )
        job.cancel()
        return 'CANCELED AND TURNING OFF'

