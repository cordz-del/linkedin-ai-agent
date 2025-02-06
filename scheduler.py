import os
import schedule
import time
from flask import Flask
from automation import LinkedInAutomation

app = Flask(__name__)
automation = LinkedInAutomation()

schedule.every().day.at("08:00").do(automation.post_on_linkedin)
schedule.every().day.at("23:00").do(automation.post_on_linkedin)
@app.route('/')
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)
    return "Scheduler is running"


pp.run(host="0.0.0.0", port=os.environ.get('PORT', 8080))
