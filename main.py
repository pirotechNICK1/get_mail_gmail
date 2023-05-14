import base64
from config import id
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Указываем авторизационные данные и инициализируем сервис Gmail
creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/gmail.compose'])
service = build('gmail', 'v1', credentials=creds)

# Задаем адрес получателя, тему и текст сообщения
to = 'адрес_получателя@gmail.com'
subject = 'Новая почта!'
body = 'Привет, это новое сообщение от меня.'

# Создаем объект MIMEText с текстом сообщения
message = MIMEText(body)

# Устанавливаем заголовки сообщения
message['to'] = to
message['subject'] = subject

# Кодируем сообщение в Base64
encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

# Создаем объект сообщения для отправки через API
message = {'raw': encoded_message}

# Отправляем сообщение через API
send_message = (service.users().messages().send(userId="me", body=message).execute())

# Выводим сообщение об успешной отправке
print(F'Сообщение успешно отправлено на адрес {to} с ID: {send_message["id"]}.')
print('id = ', id)
