import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from typing import Optional


def getenv(key: str, default: Optional[str] = None) -> str:
    value = os.getenv(key, '')
    if value == '':
        if default is not None:
            return default
        raise ValueError(f'Environment variable "{key}" is not set.')
    return value

SMTP_HOST = getenv('INPUT_SMTP_HOST')
SMTP_PORT = int(getenv('INPUT_SMTP_PORT'))
USER = f"{getenv('INPUT_ECS_ID')}@st.kyoto-u.ac.jp"
PASSWORD = getenv('INPUT_PASSWORD')
TO = getenv('INPUT_TO')
FROM = getenv('INPUT_FROM')
DATE = datetime.strptime(getenv('INPUT_DATE').strip(), "%Y%m%d")
DATE_FORMATTED = DATE.strftime(getenv('INPUT_DATE_FORMAT', "%b %d, %Y"))
PDF = getenv('INPUT_PDF')
FAMILY_NAME = getenv('INPUT_FAMILY_NAME')
GIVEN_NAME = getenv('INPUT_GIVEN_NAME')
NAME = f"{GIVEN_NAME} {FAMILY_NAME}"
SUBJECT = getenv('INPUT_SUBJECT').format(date=DATE_FORMATTED, name=NAME)
BODY = getenv('INPUT_BODY').format(date=DATE_FORMATTED, name=NAME)
SUBTYPE = getenv('INPUT_SUBTYPE', 'html')

if SUBTYPE not in ['html', 'plain']:
    raise ValueError('SUBTYPE must be "plain" or "html"')

if SUBTYPE == 'html':
    BODY += '''<p><small>This email is sent from <a href="https://github.com/tarao1006/pse-seminar-email">GitHub Actions</a>.</small></p>'''
else:
    BODY += "\nThis email is sent from GitHub Actions(https://github.com/tarao1006/pse-seminar-email)."


def main():
    msg = EmailMessage()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = SUBJECT

    with open(PDF, 'rb') as f:
        attachment = f.read()

    msg.add_alternative(BODY, SUBTYPE)
    msg.add_attachment(
        attachment,
        maintype="application",
        subtype="pdf",
        filename=f"{DATE.strftime('%Y%m%d')}_{FAMILY_NAME}.pdf"
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(USER, PASSWORD)
        smtp.send_message(msg)


if __name__ == '__main__':
    main()
