import os
import schedule
import time
from flask import Flask
from automation import LinkedInAutomation

app = Flask(__name__)
automation = LinkedInAutomation()

schedule.every().day.at("08:00").do(automation.post_on_linkedin)
schedule.every().day.at("12:00").do(automation.respond_to_comments)
schedule.every().day.at("14:00").do(automation.expand_network)
schedule.every().day.at("16:00").do(automation.engage_with_posts)
schedule.every().friday.at("10:00").do(automation.generate_weekly_article)
schedule.every().day.at("18:00").do(automation.find_hiring_professionals)
schedule.every().day.at("20:00").do(automation.celebrate_milestones)

@app.route('/')
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)
    return "Scheduler is running"

if __name__print("Port:", os.environ.get('PORT', 8080))
 == "__main__":)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 8080)
