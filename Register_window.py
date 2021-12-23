from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from Register import Register


class CreateUserFunction(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.color = [0, 0, 1, 1]
        self.black_space()
        self.label_creation()
        self.username_label()
        self.input_username()
        self.email_label()
        self.input_email()
        self.password_label()
        self.input_password()
        self.password_confirm_label()
        self.input_password_confirm()
        self.black_space()
        self.list_option_password_forget()
        self.black_space()
        self.secret_answer_label()
        self.input_secret_answers()
        self.black_space()
        self.confirm_account_creation()
        self.black_space()

    def label_creation(self):
        self.creation_message = Label(text="Create your account", color=[1, 0.49, 0, 1], size_hint=(.2, .2),
                                      pos_hint={'x': .4, 'y': 2}, font_size=25)
        self.add_widget(self.creation_message)

    # ----------------------------------------------------------- Username -----------------------------------------------------------#

    def username_label(self):
        self.message_username = Label(text="What's your username", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_username)

    def input_username(self):
        self.username_input = TextInput(text="", font_size=20, size_hint=(.4, .17),
                                        pos_hint={'x': 0.30, 'y': 2}, halign="center")
        self.add_widget(self.username_input)

    # ----------------------------------------------------------- Email -----------------------------------------------------------#

    def email_label(self):
        self.message_email = Label(text="What's your email address", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_email)

    def input_email(self):
        self.email_input = TextInput(text="", font_size=20, size_hint=(.4, .17),
                                     pos_hint={'x': 0.30}, halign="center")
        self.add_widget(self.email_input)

    # ----------------------------------------------------------- Password -----------------------------------------------------------#

    def password_label(self):
        self.message_password = Label(text="What's your password", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_password)

    def input_password(self):
        self.password_input = TextInput(text="", font_size=20, size_hint=(.4, .17),
                                        pos_hint={'x': 0.30}, halign="center", password=True)
        self.add_widget(self.password_input)

    def password_confirm_label(self):
        self.message_password_confirm = Label(text="Confirm your password", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_password_confirm)

    def input_password_confirm(self):
        self.password_confirm_input = TextInput(text="", font_size=20, size_hint=(.4, .17),
                                                pos_hint={'x': 0.30}, halign="center", password=True)
        self.add_widget(self.password_confirm_input)

    # ----------------------------------------------------------- Secret Question -----------------------------------------------------------#

    def list_option_password_forget(self):
        self.option_list = Spinner(text="Choose your question",
                                   values=("Your first pet's name", "your basics school", "your mother's name"),
                                   size_hint=(0.4, .17), pos_hint={'x': 0.3, 'y': 0.8},
                                   background_color=[1, 0.49, 0, 1])
        self.add_widget(self.option_list)

    # ----------------------------------------------------------- Secret Answer -----------------------------------------------------------#

    def secret_answer_label(self):
        self.message_secret_answer = Label(text="Introduce your answer", size_hint=(.2, .15), pos_hint={'x': 0.4})
        self.add_widget(self.message_secret_answer)

    def input_secret_answers(self):
        self.secret_answer = TextInput(text="",
                                       size_hint=(0.4, .17), pos_hint={'x': 0.3, 'y': 0.8}, font_size=20,
                                       halign="center")
        self.add_widget(self.secret_answer)

    # ----------------------------------------------------------- Button -----------------------------------------------------------#

    def confirm_account_creation(self):
        self.confirmaccountcreation = Button(text="confirm the account creation", size_hint=(.3, .2),
                                             pos_hint={'x': 0.35, 'y': 0.1}, color=[1, 1, 1, 1],
                                             background_color=[1, 0.49, 0, 1])
        self.confirmaccountcreation.bind(on_press=self.user_not_know)
        self.add_widget(self.confirmaccountcreation)

    # ----------------------------------------------------------- Space Graphic -----------------------------------------------------------#

    def black_space(self):
        self.black = Label(size_hint=(.4, .1))
        self.add_widget(self.black)

    # ----------------------------------------------------------- Function -----------------------------------------------------------#

    def user_not_know(self, instance):
        """
        create the user if all the condition are respected
        :param instance: /
        :return: /
        """
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text
        password_confirmed = self.password_confirm_input.text
        choice_question = self.option_list.text
        answer_secret_question = self.secret_answer.text.upper()
        new_user = Register(username, password, password_confirmed, email, choice_question, answer_secret_question)
        self.creation_message.text = new_user.insert_user_data_to_db
        new_user.insert_user_data_to_db


class CreateAccount(App):
    def build(self):
        Layout = CreateUserFunction()
        Layout.build()
        return Layout


if __name__ == '__main__':
    CreateAccount().run()
