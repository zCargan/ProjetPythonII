from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from PasswordForget import PasswordForget


class BoxPasswordForgot(BoxLayout):
    def build(self):
        self.title = "Password Forgot"
        self.orientation = "vertical"
        self.black_space()
        self.label_title()
        self.username_label()
        self.input_username_know()
        self.black_space()
        self.button_search_question()
        self.black_space()
        self.label_question()
        self.response_label()
        self.input_answer()
        self.password_label()
        self.input_password()
        self.black_space()
        self.change_password_button()
        self.black_space()

    # ----------------------------------------------------------- Title -----------------------------------------------------------#

    def label_title(self):
        self.title = Label(text="Password forget?", size_hint=(.2, .1), pos_hint={'x': 0.4},
                           color=[0.59, 0.239, 0.89, 1], font_size=40)
        self.add_widget(self.title)

    # ----------------------------------------------------------- Username -----------------------------------------------------------#

    def username_label(self):
        self.message_username = Label(text="Insert your username", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_username)

    def input_username_know(self):
        self.username = TextInput(text="",
                                  size_hint=(0.24, .08), pos_hint={'x': 0.38, 'y': 0.1}, halign="center")
        self.add_widget(self.username)

    def button_search_question(self):
        self.button_load_question = Button(text="Search user", size_hint=(.24, .05),
                                           pos_hint={'x': 0.38}, color=[1, 1, 1, 1],
                                           background_color=[0.59, 0.239, 0.89, 1])
        self.button_load_question.bind(on_press=self.search_and_load)
        self.add_widget(self.button_load_question)

    # ----------------------------------------------------------- central text -----------------------------------------------------------#

    def label_question(self):
        self.secret_question = Label(text='This is your secret question', size_hint=(0.24, 0.05),
                                     pos_hint={'x': 0.38, 'y': 0.1}, color=[0.59, 0.239, 0.89, 1], font_size=20)
        self.add_widget(self.secret_question)

    # ----------------------------------------------------------- secret response -----------------------------------------------------------#

    def response_label(self):
        self.message_response = Label(text="Enter your answer", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_response)

    def input_answer(self):
        self.input_answer = TextInput(text="", size_hint=(0.24, 0.07), pos_hint={'x': 0.38, 'y': 0.1}, halign="center", password=True)
        self.add_widget(self.input_answer)

    # ----------------------------------------------------------- Change Password -----------------------------------------------------------#

    def password_label(self):
        self.message_response = Label(text="Enter your new password", size_hint=(.2, .2), pos_hint={'x': 0.4})
        self.add_widget(self.message_response)

    def input_password(self):
        self.input_password = TextInput(text="", size_hint=(0.24, 0.07), pos_hint={'x': 0.38, 'y': 0.1}, halign="center",
                                      password=True)
        self.add_widget(self.input_password)

    def change_password_button(self):
        self.button_new_password = Button(text="change my password", size_hint=(.24, .06),
                                          pos_hint={'x': 0.38}, color=[1, 1, 1, 1],
                                          background_color=[0.59, 0.239, 0.89, 1])
        self.button_new_password.bind(on_press=self.check_user_informations)
        self.add_widget(self.button_new_password)

    # ----------------------------------------------------------- Space Graphic -----------------------------------------------------------#

    def black_space(self):
        self.black = Label(size_hint=(.4, .1))
        self.add_widget(self.black)

    # ----------------------------------------------------------- Function -----------------------------------------------------------#

    def search_and_load(self, instance):
        """
        return the mystery question of the user
        :param instance: /
        :return: Nothin
        """
        username = self.username.text
        question_user = PasswordForget(username)
        self.secret_question.text = question_user.search_secret_question



    def check_user_informations(self, instance):
        """
        check if the secret answer by the user is the same than in the database
        :param instance: /
        :return: /
        """
        self.answer = self.input_answer.text
        username = self.username.text
        question_user = PasswordForget(username)
        if question_user.check_secret_answer(self.answer):
            self.password = self.input_password.text
            if question_user.update_password(self.password):
                self.title.text = "Password changed!"
            else:
                self.secret_question.text = "The password need to have  minimum 8 caracteres, a digit and a letter"
        else:
            self.message_response.text = "Incorrect answer to your question"

    def change_password_user(self, instance):
        """
        change the password of the user into the database
        :param instance: /
        :return: /
        """
        self.password = self.input_answer.text
        username = self.username.text
        question_user = PasswordForget(username)
        if question_user.update_password(self.password):
            self.title.text = "Password changed!"
        else:
            self.secret_question.text = "The password need to have  minimum 8 caracteres, a digit and a letter"




class PasswordForgot(App):
    def build(self):
        Layout = BoxPasswordForgot()
        Layout.build()
        return Layout


if __name__ == '__main__':
    PasswordForgot().run()
