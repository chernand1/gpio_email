from time import time, sleep, localtime

import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText


def main():
    input_pin = 6
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    text_subtype = 'plain'

    content = """\
    Le contenu du email ici
    """

    msg = MIMEText(content, text_subtype)

    # for outlook
    serverString = 'smtp-mail.outlook.com'

    #For Gmail:
    #1- Login to your gmail account
    #2- Enable POP and IMAP in Setting (gear) --> Settings --> Forwarding and POP/IMAP
    #3- Go to https://myaccount.google.com/lesssecureapps and enable "less secure devices"
    #4- Check security events and click on "Yes" it was me trying to access my account

    #for GMAIL
    serverString = 'smtp.gmail.com'

    # arranger les addresses ici
    from_addr = "ton_email@gmail.com"
    to_addr = "nimportequel@email.com"

    password = "ton password"

    msg['Subject'] = "Sujet"
    msg['From'] = from_addr

    while(1):
        if (GPIO.input(input_pin) == 0):
            # debounce switch on IO pin
            sleep(2)
            try:
                server = smtplib.SMTP(serverString, 587)
                server.starttls()
                server.ehlo()
                server.login(from_addr, password)
                print("Login successfull")
                server.sendmail(from_addr, to_addr, msg.as_string())
                print("Email Sent")

            except Exception as e:
                print("Unable to open connection")
                print(e)

            server.close()
            print("Close connection")

if __name__ == "__main__":
    main()
