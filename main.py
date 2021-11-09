from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from connected import connected_user
# from create_accout_script import CreateUserFunction
from create_accout_window import ShowCreatingTool
from identification import dic_password, identification_user, complete_password
from mongo_connection import data_mongo


class Identification(BoxLayout):
    def build(self):
        self.title = 'Identification'
        self.orientation = "vertical"
        self.label_id()
        self.input_username_function()
        self.input_password_function()
        # self.labelPassword()
        self.button_psw_forget()
        self.button_identification()
        self.button_create_account()

    def label_id(self):
        self.identification_message = Label(text="Identification", font_size=30, color=[0, 1, 0, 1],
                                            pos_hint={'x': 0.25, 'y': 0}, size_hint=(.5, .05))
        self.add_widget(self.identification_message)

    def input_username_function(self):
        self.input_username = TextInput(text="username", font_size=20, pos_hint={'x': .38, 'y': 0},
                                        size_hint=(.24, .005))
        self.add_widget(self.input_username)

    # def labelPassword(self):
    #     self.password = Label(text="What's your password", font_size=30, color=[0, 1, 0, 1],
    #                         pos_hint={'x': 0, 'y': 0})
    #     self.add_widget(self.password)

    def input_password_function(self):
        self.input_password = TextInput(text="Password", font_size=20, pos_hint={'x': .38, 'y': 0},
                                        size_hint=(.24, .005))
        self.add_widget(self.input_password)

    def button_identification(self):
        self.confirmationButton = Button(text="Sign in", size_hint=(.2, .007),
                                         pos_hint={'x': 0.40, 'y': 0})
        self.confirmationButton.background_color = [0, 1, 0, 1]
        self.confirmationButton.bind(on_press=self.sign_in)
        self.add_widget(self.confirmationButton)

    def button_psw_forget(self):
        self.confirmationButton = Button(text="Password forget?", size_hint=(.2, .007),
                                         pos_hint={'x': 0.40, 'y': 0})
        self.confirmationButton.background_color = [0, 1, 0, 1]
        self.confirmationButton.bind(on_press=self.password_forget)
        self.add_widget(self.confirmationButton)

    def button_create_account(self):
        self.create_account_button = Button(text="Create account?", size_hint=(.2, .007),
                                            pos_hint={'x': 0.40, 'y': 0})
        self.create_account_button.background_color = [0, 1, 0, 1]
        self.create_account_button.bind(on_press=self.create_account)
        self.add_widget(self.create_account_button)

    def sign_in(self, instance):
        """
        check is the username and the password are corrects, if is, show the message "connected"
        :param instance:
        :return: the type of connection (yes or not)
        """
        user = self.input_username.text
        password = self.input_password.text
        self.identification_message.text = connected_user(identification_user(data_mongo(), user, password))
        self.identification_message.color = [0, 1, 0, 1]

    def password_forget(self):
        pass

    def create_account(self, instance):
        """
        run the page of creation's account
        :param instance:
        :return: the user's datas to the database
        """
        ShowCreatingTool().run()


class CheckUser(App):
    def build(self):
        Layout = Identification()
        Layout.build()
        return Layout


if __name__ == '__main__':
    CheckUser().run()

    # if user not in dic_password:
    #     print("user not found")
    # elif dic_password[user][0] != password:
    #     print("incorrect password")
    # else:
    #     print("Successful authentication")
