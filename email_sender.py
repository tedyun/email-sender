import argparse
import smtplib
from email.headerregistry import Address
from email.message import EmailMessage
from typing import Union, Sequence


USERNAME_FILE_NAME = 'username'
PWD_FILE_NAME = 'pass'
TEST_EMAIL_FILE_NAME = 'test_email'
GMAIL_SMTP_URL = 'smtp.gmail.com'
GMAIL_SMTP_PORT = 465
DEFAULT_SUBJECT = 'Test email subject from Python Bot'
DEFAULT_CONTENT = 'Test email content from Python Bot.'
DEFAULT_FROM_NAME = "Ted's Bot"

def read_from_file(fpath):
  with open(fpath, 'rt') as f:
    return f.read().strip()


def parse_args():
    parser = argparse.ArgumentParser(description='Send args.')
    parser.add_argument('--to_addr', help='The TO address.', default=read_from_file(TEST_EMAIL_FILE_NAME))
    parser.add_argument('--subject', help='The subject.', default=DEFAULT_SUBJECT)
    parser.add_argument('--content', help='The content.', default=DEFAULT_CONTENT)
    parser.add_argument('--from_name', help='The content.', default=DEFAULT_FROM_NAME)
    args = parser.parse_args()
    print('Input args:')
    for arg in vars(args):
        print('--{}: {}'.format(arg, getattr(args, arg)))
    return args


def send_email(to_addrs: Union[str, Sequence[str]], subject: str, content: str,
               smtp_url: str = GMAIL_SMTP_URL, smtp_port: int = GMAIL_SMTP_PORT,
               from_name: str = ''):
  if isinstance(to_addrs, str):
    to_addrs = [to_addrs]

  from_email = read_from_file(USERNAME_FILE_NAME)
  pwd = read_from_file(PWD_FILE_NAME)

  msg = EmailMessage()
  msg['Subject'] = subject
  if from_name:
    msg['From'] = Address(display_name=from_name, addr_spec=from_email)
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
  args = parse_args()
  send_email(
    to_addrs=args.to_addr,
    subject=args.subject,
    content=args.content,
    from_name=args.from_name,
  )

if __name__ == "__main__":
  main()
