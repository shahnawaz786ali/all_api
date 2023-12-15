from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings

@shared_task(bind=True)
def test_func(self,email,filename):
    subject = 'My Data'
    body = 'Please find attached Data File.'
    email = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [email]) #Specify Valid Email in settings.py
    email.attach_file(filename)
    email.send()
    return "Email Sent"