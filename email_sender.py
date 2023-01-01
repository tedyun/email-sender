from typing import Union, Sequence
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address

USERNAME_FILE_NAME = 'username'
PWD_FILE_NAME = 'pass'
TEST_EMAIL_FILE_NAME = 'test_email'
GMAIL_SMTP_URL = 'smtp.gmail.com'
GMAIL_SMTP_PORT = 465


def read_from_file(fpath):
  with open(fpath, 'rt') as f:
    return f.read().rstrip()


def send_email(to_addrs: Union[str, Sequence[str]], subject: str, content: str,
               smtp_url: str = GMAIL_SMTP_URL, smtp_port: int = GMAIL_SMTP_PORT,
               from_display_name: str = ''):
  if isinstance(to_addrs, str):
    to_addrs = [to_addrs]

  from_email = read_from_file(USERNAME_FILE_NAME)
  pwd = read_from_file(PWD_FILE_NAME)

  msg = EmailMessage()
  msg['Subject'] = subject
  # me == the sender's email address
  # family = the list of all recipients' email addresses
  if from_display_name:
    msg['From'] = Address(display_name=from_display_name, addr_spec=from_email)
  else:
    msg['From'] = from_email
  msg['To'] = ', '.join(to_addrs)
  # msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
  msg.set_content(content)

  connection = smtplib.SMTP_SSL(smtp_url, smtp_port)  
  connection.login(from_email, pwd)
  connection.send_message(msg=msg, from_addr=from_email, to_addrs=to_addrs)
  connection.close()


def main():
  send_email(
    to_addrs=read_from_file(TEST_EMAIL_FILE_NAME),
    subject='Test email from Python bot4',
    content='Email test.',
    from_display_name="Ted's Bot",
  )

if __name__ == "__main__":
  main()
