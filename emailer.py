import smtplib

class Emailer:
    def __init__(self, sender, pw, receiver):
        self.sender = sender
        self.sender_p = pw
        self.receiver = receiver
        self.smtp_host = 'smtp.gmail.com'
        self.smtp_port = 587

    def _send_email(self, message):
        s = smtplib.SMTP(self.smtp_host, self.smtp_port)
        s.starttls()
        s.login(self.sender, self.sender_p)
        s.sendmail(self.sender, self.receiver, message)
        s.quit()

    def send_email(self,subject,message):
        email = f'Subject: {subject}\n\n{message}\n'
        self._send_email(email)