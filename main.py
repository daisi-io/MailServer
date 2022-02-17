import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For gmail use, go to the account settings 
# and allow less secure apps to access the account:
# https://myaccount.google.com/lesssecureapps


def send_email(user:str, password:str, to:str, subject:str="", body:str="", smtp_server_host="smtp.gmail.com"):
    # to = [to]
    # email_text = f"""\
    # From: {user}
    # To: {", ".join(to)}
    # Subject: {subject}

    # {body}
    # """
    
    # print("sending email: ")
    # print(email_text)

    # server = smtplib.SMTP(smtp_server_host, 587)
    # server.starttls()
    # server.login(user, password)
    # server.sendmail(user, to, email_text)
    # server.quit()

    try:
        connection = smtplib.SMTP(host=smtp_server_host, port=587)
        connection.starttls()
        connection.login(user, password)

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = to

        # Create the body of the message (a plain-text and an HTML version).

        # Record the MIME types of both parts - text/plain and text/html.
        html_message = MIMEText(body, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(html_message)

        connection.sendmail(user, to, msg.as_string())
        connection.quit()
    except smtplib.SMTPAuthenticationError as e:
        print(e)


    return "success"

