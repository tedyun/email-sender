## Simple Email Sender using SMTP in Python

Need to create three text files:
* `username`: your email address/username
* `pass`: your password (for Gmail, generate an App Password for this after enabling 2-factor authorization)
* `test_email`: an email address to receive test messages by default.

Example 1 (simplest example):
```
$ python3 email_sender.py \
  --subject "Email test subject" \
  --content "Email test content from command line."
```

Example 2 (with cc, bcc, and custom name):
```
$ python3 email_sender.py \
  --to "email1@domain.com,email2@domain.com" \
  --cc "email3@domain.com,email4@domain.com" \
  --bcc "email5@domain.com,email6@domain.com" \
  --from_name "Email bot name" \
  --subject "Email subject" \
  --content "Email content."
```

Example 3 (send current public IP address):
```
$ python3 email_sender.py \
  --subject "current ip" \
  --content "$(curl https://ipinfo.io/ip)"
```
