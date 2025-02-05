import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'

# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = '+1234567890'

# Notification recipient
RECIPIENT_EMAIL = 'r.aarongraham.wv@gmail.com'
RECIPIENT_PHONE_NUMBER = '+13049109804'


def send_email_notification(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USERNAME
    msg['To'] = RECIPIENT_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, RECIPIENT_EMAIL, msg.as_string())


def send_sms_notification(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=RECIPIENT_PHONE_NUMBER
    )


def notify_captcha_encountered():
    subject = 'CAPTCHA Encountered'
    message = 'A CAPTCHA was encountered during the LinkedIn automation process. Please solve it manually.'
    send_email_notification(subject, message)
    send_sms_notification(message)
