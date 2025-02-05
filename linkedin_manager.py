import requests

# Use the extracted li_at cookie
li_at_cookie = "your_li_at_cookie_value"

# Set up session with the cookie
session = requests.Session()
session.cookies.set("li_at", li_at_cookie, domain=".linkedin.com")

# Function to post an update on LinkedIn
def post_update(content):
    url = "https://www.linkedin.com/voyager/api/feed/updates"
    headers = {
        "csrf-token": session.cookies.get("JSESSIONID").strip('"'),
        "Content-Type": "application/json",
    }
    data = {
        "content": content,
        "visibility": "PUBLIC",
    }
    response = session.post(url, headers=headers, json=data)
    return response.status_code
