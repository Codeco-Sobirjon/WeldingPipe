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
    <h1>Подробности новой заявки</h1>
    <p><strong>Полное имя:</strong> {full_name}</p>
    <p><strong>Телефон:</strong> {phone}</p>
    <p><strong>Название компании:</strong> {company_name}</p>
    <p><strong>Комментарий:</strong> {comment}</p>
    <h2>Прикрепленные файлы:</h2>
    <ul>
        <li><a href="{file1_url}" download>Скачать</a></li>
        <li><a href="{file2_url}" download>Скачать</a></li>
    </ul>
    <p>Отправлено из armsnab74.ru</p>
    '''

    recipient_list = ['Gain11@mail.ru']   # Replace with the recipient's email

    email = EmailMessage(
        subject,
        html_content,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
    )
    email.content_subtype = 'html'  # Set the email content type to HTML
    email.send()