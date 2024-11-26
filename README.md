## Simple Email Sender using SMTP in Python

Need to create three text files:
* `username`: your email address/username
* `pass`: your password (for Gmail, generate an App Password for this after enabling 2-factor authorization)
* `test_email`: an email address to receive test messages by default.

Example 1:
```
$ python3 email_sender.py \
  --subject "Email test subject" \
  --content "Email test content from command line."
```

Example 2:
```
$ python3 email_sender.py \
  --to_addr "email@domain.com" \
  --from_name "Email bot name" \
  --subject "Email subject" \
  --content "Email content."
```
