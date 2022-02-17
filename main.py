import smtplib

# For gmail use, go to the account settings 
# and allow less secure apps to access the account:
# https://myaccount.google.com/lesssecureapps


def send_email(user:str, password:str, to:str, subject:str="", body:str="",):
    to = [to]
    email_text = f"""\
    From: {user}
    To: {", ".join(to)}
    Subject: {subject}

    {body}
    """
    
    print("sending email: ")
    print(email_text)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.sendmail(user, to, email_text)
    server.quit()
    
    return "success"
