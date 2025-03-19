import random
from django.core.mail import send_mail

def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))

def send_verification_email(email, code):
    subject = 'Email Verification Code'
    message = f'Your verification code is: {code}'
    send_mail(subject, message, 'admin@mylogsapp.com', [email])
