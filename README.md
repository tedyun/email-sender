## Simple Email Sender using SMTP in Python

Need to create three files:
* `username`: your email address/username
* `pass`: your password (for Gmail, generate an App Password for this after enabling 2-factor authorization)
* `test_email`: an email address to receive test messages by default.

Example:
```
$ python3 email_sender.py \
  --subject "Email test subject" \
  --content "Email test content from command line."
```
