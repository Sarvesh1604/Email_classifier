import sqlite3
from email import policy
from email.parser import BytesParser

conn = sqlite3.connect('db.sqlite3')

cur = conn.execute('''SELECT email from Add_Emails_upload_emails;''')
email = cur.fetchall()[0]
with open(email[0], 'rb') as fp:
    name = fp.name  # Get file name
    msg = BytesParser(policy=policy.default).parse(fp)
text = msg.get_body(preferencelist=('plain')).get_content()

print(text)