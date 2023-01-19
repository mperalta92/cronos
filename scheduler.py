from flask_apscheduler import APScheduler
from datetime import datetime


scheduler_main = APScheduler()

@scheduler_main.task('interval', id='do_deamon_task', seconds=1, misfire_grace_time=1000)
def deamon_task():
	#print(f"hola son las {datetime.now()}!")
	pass