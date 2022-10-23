import PySimpleGUI as sg


class UI:
    def __init__(self):
        """
        It creates a GUI window with a few buttons and text fields
        """
        self.__window = None
        sg.theme('DarkAmber')
        self.__layout = [
            [sg.Text('Email:'), sg.Push(), sg.InputText(key='-email-')],
            [sg.Text('Password:'), sg.Push(), sg.InputText(key='-password-')],
            [sg.Text('Status:'), sg.Text(key='-status-'), sg.Push(), sg.Button('Login')],
            [sg.Button('Load Emails', size=20), sg.Text('Loaded Emails:'), sg.Text(key='-LoadedEmails-'),
             sg.Text('Amount of Mails: '), sg.InputText(key='-amountEmail-', size=15)],
            [sg.Text('Text:'), sg.Push(), sg.InputText(key='-text-')],
            [sg.Text('Successful:'), sg.Text(key='-emailValid-'), sg.Text('Unsuccessful:'),
             sg.Text(key='-emailInvalid-'), sg.Push(), sg.Button('Start mailing', size=20)]
        ]

    def startUI(self):
        """
        It creates a window object, and assigns it to the variable self.__window
        """
        self.__window = sg.Window('MassMailer', self.__layout, finalize=True)
        self.__window['-status-'].update('Not connected...')
        self.__window['-LoadedEmails-'].update('0')
        self.__window['-emailValid-'].update('0')
        self.__window['-emailInvalid-'].update('0')
        self.__window['-amountEmail-'].update('20')

    def getUI(self):
        """
        It returns the window object of the class
        :return: The window is being returned.
        """
        return self.__window

    def closeUI(self):
        """
        It closes the UI window
        """
        self.__window().close()
