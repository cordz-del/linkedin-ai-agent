import os
import schedule
import time
from automation import LinkedInAutomation

automation = LinkedInAutomation()

schedule.every().day.at("08:00").do(automation.post_on_linkedin)
schedule.every().day.at("23:00").do(automation.post_on_linkedin)

while True:
    schedule.run_pending()
    time.sleep(60)

