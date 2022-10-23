import smtplib


class Server:
    def __init__(self):
        """
        It initializes the class.
        """
        self.__user = None
        self.__pass = None
        self.__port = 587
        self.__smtp = "smtp.gmail.com"
        self.__server = smtplib.SMTP(self.__smtp, self.__port)

    def start(self):
        """
        It starts the TLS connection
        """
        try:
            self.__server.starttls()
            return True
        except smtplib.SMTPHeloError:
            return False

    def login(self, user, password):
        """
        It takes a user and password, sets the user and password to the class variables, and then tries to login to the
        server. If it succeeds, it returns True, otherwise it returns False

        :param user: The email address you want to send from
        :param password: The password of the email account you're using to send the email
        :return: True or False
        """
        self.__user = user
        self.__pass = password

        try:
            self.__server.login(user=self.__user, password=self.__pass)
            return True
        except smtplib.SMTPAuthenticationError:
            return False

    def sendmail(self, receiver, message):
        """
        It sends an email to the receiver with the message

        :param receiver: The email address of the person you want to send the email to
        :param message: The message to be sent
        :return: True or False
        """
        try:
            self.__server.sendmail(from_addr=self.__user, to_addrs=receiver, msg=message)
            return True
        except smtplib.SMTPRecipientsRefused:
            return False
        except smtplib.SMTPSenderRefused:
            return False

    def stop(self):
        """
        It closes the server
        """
        self.__server.close()
