import PySimpleGUI as sg

from Core import Server, GUI


def sendMails():
    """
    It sends an email to every email in the emails list, the amount of times specified in the values dictionary
    """
    for i in range(int(values['-amountEmail-'])):
        for email in emails:
            sendMail(email)


def sendMail(email):
    """
    It sends an email to the address specified in the `email` parameter, and if it fails, it tries again up to 3 times

    :param email: The email address to send the email to
    """
    maxRetries = 3
    while maxRetries > 0:
        if server.sendmail(email, values['-text-']):
            View['-emailValid-'].update(str(int(values['-emailValid-'] + 1)))
            break
        else:
            maxRetries += 1
            View['-emailInvalid-'].update(str(int(values['-emailInvalid-'] + 1)))


def loadEmails():
    """
    It opens a file dialog, reads the file, and returns the file content
    :return: The file content is being returned.
    """
    file = sg.filedialog.askopenfile()
    if file:
        fileContent = file.readlines()
        if len(emails) > 0:
            View['-LoadedEmails-'].update(str(len(emails)))
        return fileContent


def checkLogin():
    """
    If the email and password fields are not empty, then try to login to the server with the email and password. If it
    works, then update the status label to say that the server is online and the account is connected. If it doesn't work,
    then update the status label to say that the server is online but the account could not be connected
    """
    if not values['-email-'] is None and not values['-password-'] is None:
        if server.login(values['-email-'], values['-password-']):
            View['-status-'].update('Server online | Account connected')
            print(values['-email-'] + " " + values['-password-'])
        else:
            View['-status-'].update('Server online | Could not connect with account. Wrong Combination?')


if __name__ == '__main__':
    window = GUI.UI()
    window.startUI()
    View = window.getUI()
    server = Server.Server()
    emails = []

    if server.start():
        View['-status-'].update('Server online')
    else:
        View['-status-'].update('Server could not start. Try to launch again!')

    while True:
        event, values = View.read()

        match event:
            case 'Login':
                checkLogin()

            case 'Load Emails':
                emails = loadEmails()

            case 'Start mailing':
                if int(str(values['-amountEmail-'])) > 0 and len(values['-text-']) > 0 and len(emails) > 0:
                    View['-status-'].update('Server online | Started sending mails')
                    sendMails()

            case sg.WIN_CLOSED:
                window.closeUI()
                break
