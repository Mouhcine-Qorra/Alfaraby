from termcolor import colored
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


def sendEmail(Name="", Email="", Message=""):

    # Create the root message and fill in the from, to, and subject headers
    sender = 'contact@maweb.ma'
    recipients = ["dmimadb76@outlook.com", "qorra.mouhcine1@gmail.com"]
    print(f"Sending to :\t\t{recipients}")
    print('\tGetting Parameters...')
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = f'Formulaire Soumis le {datetime.datetime.now().strftime("%d/%m/%Y")}'
    msgRoot['From'] = sender
    msgRoot["To"] = ", ".join(recipients)
    password = 'Taro@987654'
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgalternative = MIMEMultipart('alternative')
    msgRoot.attach(msgalternative)

    hour = int(datetime.datetime.now().strftime("%H"))
    hour = '00' if hour + 1 == 24 else hour
    plain = f"""\Bonjour Alfaraby,

Veuillez trouver ci-dessous les cordonnées d'un nouveau client Soumis la Formulaire le \
{datetime.datetime.now().strftime("%Y/%m/%d à "+ str(hour) +":%M")}.

Name    : {Name}
Email   : {Email}
Message : {Message}


Cordialement,
Maweb Solutions
maweb.ma
    """
    msgtext = MIMEText(plain, 'plain')
    msgalternative.attach(msgtext)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    html = f"""\
    Bonjour Alfaraby,<br><br><br>

    <p style="margin-left:.5rem">Veuillez trouver ci-dessous les cordonnées d'un nouveau client Soumis la Formulaire le \
    {datetime.datetime.now().strftime("%Y/%m/%d à "+ str(hour) +":%M")}.</p><br>
    
    <p style="margin-left:1rem">Name    : {Name}</p>
    <p style="margin-left:1rem">Email   : {Email}</p>
    <p style="margin-left:1rem">Message : {Message}</p><br>
    

    Cordialement,<br>
    Maweb Solutions<br>
    maweb.ma<br><br>
    """
    msgtext = MIMEText(html, 'html')
    msgalternative.attach(msgtext)

    print('\tConnecting to Zoho Mail...')
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    try:
        print('\tlogin to your account...')
        server.login(sender, password)
        print('\tSending email...')
        server.sendmail(sender, recipients, msgRoot.as_string())
        print(f'\t{colored("Email sent successfully", "green")}')
    except Exception as e:
        print(f'\tPROBLEM: {e}...\n')
    finally:
        server.quit()
        print('\tQuit...')


