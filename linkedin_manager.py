from linkedin_api import Linkedin
from config import LINKEDIN_USERNAME, LINKEDIN_PASSWORD

linkedin = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)

def post_update(content):
    linkedin.post_update(content)

def get_profile_updates():
    return linkedin.get_profile_updates(LINKEDIN_USERNAME)

def get_comments(post_id):
    return linkedin.get_comments(post_id)

def comment_on_post(post_id, comment):
    linkedin.comment_on_post(post_id, comment)

def search_people(query):
    return linkedin.search_people(query)

def add_connection(profile_id):
    linkedin.add_connection(profile_id)

def search_feed(query):
    return linkedin.search_feed(query)

def send_message(profile_id, message):
    linkedin.send_message(profile_id, message)

def get_feed():
    return linkedin.get_feed()
