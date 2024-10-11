from django.conf import settings
from django.core.mail import EmailMessage


def send_html_email():
    subject = 'HTML Test Email'
    html_content = '<h1>This is a test email</h1><p>Sent from Django!</p>'
    recipient_list = ['Gain11@mail.ru']  # Replace with the recipient's email

    email = EmailMessage(
        subject,
        html_content,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
    )
    email.content_subtype = 'html'  # Set the email content type to HTML
    email.send()