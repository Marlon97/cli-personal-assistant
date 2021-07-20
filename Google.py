import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_message(to, subject, message_text):
    """Create a message for an email.

    Args:
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = to
    mimeMessage['subject'] = subject
    mimeMessage.attach(MIMEText(message_text, 'html'))
    return base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()


def sender(service, message):
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    message: Message to be sent.

    Returns:
    1 if message was sent.
    -1 if message wasn't sent.
    """
    try:
        message = service.users().messages().send(
            userId='me',
            body={'raw': message}).execute()
        return 1
    except:
        print('An error occurred: Sending Message')
        return -1


def send_message(to, subject, message_text):
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentialsGM.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    # Call the Gmail API
    message = create_message(to, subject, message_text)
    sender(service, message)

