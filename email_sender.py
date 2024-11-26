import argparse
import smtplib
from email.headerregistry import Address
from email.message import EmailMessage
from typing import Any, Sequence


USERNAME_FILE_NAME = 'username'
PWD_FILE_NAME = 'pass'
TEST_EMAIL_FILE_NAME = 'test_email'
GMAIL_SMTP_URL = 'smtp.gmail.com'
GMAIL_SMTP_PORT = 465
DEFAULT_SUBJECT = 'Test email subject from Python Bot'
DEFAULT_CONTENT = 'Test email content from Python Bot.'
DEFAULT_FROM_NAME = "Ted's Bot"

def read_from_file(fpath: str) -> str:
  with open(fpath, 'rt') as f:
    return f.read().strip()


def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(description='Email args.')
  parser.add_argument('--to', help='Comma-separated list of TO addresses.',
                      default=read_from_file(TEST_EMAIL_FILE_NAME), type=str)
  parser.add_argument('--subject', help='Subject.', default=DEFAULT_SUBJECT)
  parser.add_argument('--content', help='Content.', default=DEFAULT_CONTENT)
  parser.add_argument('--from_name', help='Display name of the sender.',
                      default=DEFAULT_FROM_NAME)
  parser.add_argument('--cc', help='Comma-separated list of cc addresses.',
                      default='', type=str)
  parser.add_argument('--bcc', help='Comma-separated list of bcc addresses.',
                      default='', type=str)
  args = parser.parse_args()
  print('Input args:')
  for arg in vars(args):
    print('--{}: {}'.format(arg, getattr(args, arg)))
  return args


def send_email(to: str, subject: str, content: str, from_name: str, cc: str,
               bcc: str,
               smtp_url: str = GMAIL_SMTP_URL, smtp_port: int = GMAIL_SMTP_PORT,
               ) -> None:
  from_email = read_from_file(USERNAME_FILE_NAME)
  pwd = read_from_file(PWD_FILE_NAME)

  msg = EmailMessage()
  msg.set_content(content)

  msg['Subject'] = subject
  if from_name:
    msg['From'] = Address(display_name=from_name, addr_spec=from_email)
  else:
    msg['From'] = from_email
  msg['To'] = to
  if cc:
    msg['Cc'] = cc
  if bcc:
    msg['Bcc'] = bcc
  # msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'  

  connection = smtplib.SMTP_SSL(smtp_url, smtp_port)
  connection.login(from_email, pwd)
  connection.send_message(msg=msg)
  connection.close()


def main():
  args = parse_args()
  send_email(
    to=args.to,
    subject=args.subject,
    content=args.content,
    from_name=args.from_name,
    cc=args.cc,
    bcc=args.bcc,
  )

if __name__ == "__main__":
  main()
