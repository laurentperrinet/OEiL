#!/usr/bin/env python3

#import cgi, os, datetime, re
import smtplib
from email.mime.text import MIMEText

DATA_DIR = './data'             # the directory in which to put the data file
SUFFIX = 'dat'
EMAIL_FROM = 'Laurent Perrinet <laurent@spik.xyz>'
EMAIL_SMTP = 'localhost'

fs = 'hello world'
email = 'laurent.perrinet@univ-amu.fr'
msg = MIMEText(fs)
msg['Subject'] = 'data from on-line experiment'
msg['From'] = EMAIL_FROM
msg['To'] = email

print(msg)
s = smtplib.SMTP(EMAIL_SMTP)
s.sendmail(EMAIL_FROM, [email], msg.as_string())
s.quit()
