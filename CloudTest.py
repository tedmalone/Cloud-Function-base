import pandas as pd
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Initialize some variables
EMAIL_ME = os.getenv("EMAIL_ME")
EMAIL_YOU = os.getenv("EMAIL_YOU")
EMAIL_PWD = os.getenv("EMAIL_PWD")

# Scrape the list of Gainers from Yahoo
# Use head(10) to reduce list to Top-10
URL = "https://finance.yahoo.com/gainers"
table = pd.read_html(URL, attrs = {'class' : 'W(100%)'})
df = table[0].head(10).set_index('Symbol')

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Top Gainers"
msg['From'] = EMAIL_ME
msg['To'] = EMAIL_YOU

# Create the body of the message (a plain-text and an HTML version).
text = df.to_string()
html = df.to_html()

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Login, send the message, and quit.
mail = smtplib.SMTP_SSL('smtp.gmail.com',465)
mail.login(EMAIL_ME,EMAIL_PWD)
mail.sendmail(EMAIL_ME,EMAIL_YOU,msg.as_string())
mail.quit()