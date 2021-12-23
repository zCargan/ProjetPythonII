from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Connection import Connection
from PasswordForget_window import PasswordForgot


class BoxIdentification(BoxLayout):
    def build(self):
        self.title = 'Identification'
        self.orientation = "vertical"
        self.black_space()
        self.label_id()
        self.black_space()
        self.black_space()
        self.username_label()
        self.input_username_function()
        self.black_space()
        self.password_label()
        self.input_password_function()
        self.button_psw_forget()
        self.black_space()
        self.black_space()
        self.black_space()
        self.black_space()
        self.button_identification()
        self.black_space()
        self.button_create_account()
        self.black_space()

    def label_id(self):
        self.identification_message = Label(text="Identification", font_size=40, color=[1, 0.49, 0, 1],
                                            pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.identification_message)

    # ----------------------------------------------------------- Username -----------------------------------------------------------#

    def username_label(self):
        self.label_username = Label(text="Enter your username", size_hint=(.2, .01), pos_hint={'x': 0.4, 'y': 0.7})
        self.add_widget(self.label_username)

    def input_username_function(self):
        self.input_username = TextInput(text="", font_size=20, pos_hint={'x': .38, 'y': 0},
                                        size_hint=(.24, .011), halign="center")
        self.add_widget(self.input_username)

    # ----------------------------------------------------------- Password -----------------------------------------------------------#

    def password_label(self):
        self.label_password = Label(text="Enter your password", size_hint=(.2, .01), pos_hint={'x': 0.4, 'y': 0.7})
        self.add_widget(self.label_password)

    def input_password_function(self):
        self.input_password = TextInput(text="", font_size=20, pos_hint={'x': .38, 'y': 0},
                                        size_hint=(.24, .011), halign="center", password=True)
        self.add_widget(self.input_password)

    # ----------------------------------------------------------- Space Graphic -----------------------------------------------------------#

    def black_space(self):
        self.black = Label(size_hint=(.4, .01))
        self.add_widget(self.black)

    # ----------------------------------------------------------- Button -----------------------------------------------------------#

    def button_psw_forget(self):
        self.confirmationButton = Button(text="Password forget?", size_hint=(.2, .01),
                                         pos_hint={'x': 0.40, 'y': 0}, color=[1, 0.49, 0, 1])
        self.confirmationButton.background_color = [0, 1, 0, 0]
        self.confirmationButton.bind()
        self.add_widget(self.confirmationButton)

    def button_identification(self):
        self.confirmationButton = Button(text="Sign in", size_hint=(.2, .01),
                                         pos_hint={'x': 0.40, 'y': 0})
        self.confirmationButton.background_color = [1, 0.49, 0, 1]
        self.confirmationButton.bind(on_press=self.sign_in)
        self.add_widget(self.confirmationButton)

    def button_create_account(self):
        self.create_account_button = Button(text="Create account?", size_hint=(.2, .01),
                                            pos_hint={'x': 0.40, 'y': 0}, color=[1, 0.49, 0, 1])
        self.create_account_button.background_color = [0, 1, 0, 0]
        self.create_account_button.bind(on_press=self.create_account)
        self.add_widget(self.create_account_button)

    # ----------------------------------------------------------- Function -----------------------------------------------------------#

    def sign_in(self, instance):
        """
        check if the username and the password are corrects, if is, show the message "connected"
        :param instance:
        :return: the type of connection (yes or not)
        """
        user = self.input_username.text
        password = self.input_password.text
        User_connected = Connection(user, password)
        # print(User_connected.check_password)
        if User_connected.check_password:
            self.identification_message.text = "Connected"
            return 1
        else:
            self.identification_message.text = "Username or password invalid"


    def password_forget(self):
        pass

    def create_account(self, instance):
        pass


class Identification(App):
    def build(self):
        Layout = BoxIdentification()
        Layout.build()
        return Layout


if __name__ == '__main__':
    Identification().run()
