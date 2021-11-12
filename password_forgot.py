from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from mongo_connection import defined_id_user, change_password_user, is_strong_password
from mongo_connection import data_mongo, check_hashed


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
        self.black_space()
        self.button_check_answer()
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
                                  size_hint=(0.24, .07), pos_hint={'x': 0.38, 'y': 0.1}, halign="center")
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
        self.input_answer = TextInput(text="", size_hint=(0.24, 0.07), pos_hint={'x': 0.38, 'y': 0.1}, halign="center")
        self.add_widget(self.input_answer)

    def button_check_answer(self):
        self.button_check = Button(text="check my answer", size_hint=(.24, .06),
                                   pos_hint={'x': 0.38}, color=[1, 1, 1, 1], background_color=[0.59, 0.239, 0.89, 1])
        self.button_check.bind(on_press=self.check_user_informations)
        self.add_widget(self.button_check)

    # ----------------------------------------------------------- Change Password -----------------------------------------------------------#

    def change_password_button(self):
        self.button_new_password = Button(text="change my password", size_hint=(.24, .06),
                                          pos_hint={'x': 0.38}, color=[1, 1, 1, 1],
                                          background_color=[0.59, 0.239, 0.89, 1])
        self.button_new_password.bind(on_press=self.change_password_user)
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
        dic_user = data_mongo()
        if username in dic_user:
            question = dic_user[username][4]
            self.secret_question.text = "Your secret question is : " + question

    def check_user_informations(self, instance):
        """
        check if the secret answer by the user is the same than in the database
        :param instance: /
        :return: /
        """
        dic_user = data_mongo()
        username_give = self.username.text
        answer_give = self.input_answer.text.upper()
        answed_crypted = bytes(answer_give, encoding="utf-8")
        if username_give not in dic_user:
            self.secret_question.text = "User not found"
        else:
            if check_hashed(answed_crypted, dic_user[username_give][5]):
                self.message_response.text = "Correct! Enter your new password"
                self.input_answer.text = ""
            else:
                self.message_response.text = "Incorrect answer"

    def change_password_user(self, instance):
        """
        change the password of the user into the database
        :param instance: /
        :return: /
        """
        username = self.username.text
        password = self.input_answer.text
        if is_strong_password(password):
            change_password_user(username, password)
            self.secret_question.text = ""
            self.message_response.text = ""
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
