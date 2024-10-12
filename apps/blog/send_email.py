import mimetypes
from django.core.mail import EmailMessage
from django.conf import settings
import mimetypes, mimetypes


def send_html_email(full_name, phone, company_name, comment, file1, file2):
    # Construct the URLs for the files
    file1_url = f'https://armsnab74.ru/media/file1/{file1}'
    file2_url = f'https://armsnab74.ru/media/file2/{file2}'  # Corrected the URL for file2
    subject = 'New Submission from ' + full_name  # Add a subject based on the user's name

    # Create the HTML content with links to the files
    html_content = f'''
    <h1>New Submission Details</h1>
    <p><strong>Full Name:</strong> {full_name}</p>
    <p><strong>Phone:</strong> {phone}</p>
    <p><strong>Company Name:</strong> {company_name}</p>
    <p><strong>Comment:</strong> {comment}</p>
    <h2>Attached Files:</h2>
    <ul>
        <li><a href="{file1_url}" download>Download File 1</a></li>
        <li><a href="{file2_url}" download>Download File 2</a></li>
    </ul>
    <p>Sent from Django!</p>
    '''

    recipient_list = ['sobirjon.bobojonov@mail.ru']  # Replace with the recipient's email

    email = EmailMessage(
        subject,
        html_content,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
    )
    email.content_subtype = 'html'  # Set the email content type to HTML
    email.send()