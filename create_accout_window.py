from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from mongo_connection import data_mongo, user_already_know, email_already_know, same_password, is_strong_password, \
    number_user, collection, create_data_to_db


class CreateUserFunction(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.label_creation()
        # self.label_username()
        self.input_username()
        self.input_first_name()
        self.input_last_name()
        self.input_email()
        self.input_password()
        self.input_password_confirm()
        self.confirm_account_creation()

    def label_creation(self):
        self.creation_message = Label(text="Create your account")
        self.add_widget(self.creation_message)

    # def label_username(self):
    #     self.username_message = Label(text="What's your username?", color=[0, 1, 0, 1])
    #     self.add_widget(self.label_username())

    def input_username(self):
        self.username_input = TextInput(font_size=20, size_hint=(.4, .35),
                                        pos_hint={'x': 0.30})
        self.add_widget(self.username_input)

    def input_first_name(self):
        self.first_name_input = TextInput(text="What's your first name?", font_size=20, size_hint=(.4, .4),
                                          pos_hint={'x': 0.30})
        self.add_widget(self.first_name_input)

    def input_last_name(self):
        self.last_name_input = TextInput(text="What's your last name?", font_size=20, size_hint=(.4, .4),
                                         pos_hint={'x': 0.30})
        self.add_widget(self.last_name_input)

    def input_email(self):
        self.email_input = TextInput(text="What's your email address?", font_size=20, size_hint=(.4, .4),
                                     pos_hint={'x': 0.30})
        self.add_widget(self.email_input)

    def input_password(self):
        self.password_input = TextInput(text="What's your password?", font_size=20, size_hint=(.4, .4),
                                        pos_hint={'x': 0.30})
        self.add_widget(self.password_input)

    def input_password_confirm(self):
        self.password_confirm_input = TextInput(text="Confirm your password?", font_size=20, size_hint=(.4, .4),
                                                pos_hint={'x': 0.30})
        self.add_widget(self.password_confirm_input)

    def confirm_account_creation(self):
        self.confirmaccountcreation = Button(text="confirm the account creation", size_hint=(.3, .4),
                                             pos_hint={'x': 0.35}, color=[0, 1, 0, 1])
        self.confirmaccountcreation.bind(on_press=self.user_not_know)
        self.add_widget(self.confirmaccountcreation)

    def user_not_know(self, instance):
        """
        create the user if all the condition are respected
        :param instance: /
        :return: /
        """
        username = self.username_input.text
        first_name = self.first_name_input.text
        last_name = self.last_name_input.text
        email = self.email_input.text
        password = self.password_input.text
        password_confirmed = self.password_confirm_input.text
        if user_already_know(username):
            self.creation_message.text = ("this username is already taken")
        else:
            if email_already_know(email):
                self.creation_message.text = ("This email address is already register")
            else:
                if same_password(password, password_confirmed):
                    if is_strong_password(password):
                        create_data_to_db(username, first_name, last_name, email, password, password_confirmed)
                        self.creation_message.text =("Register!")
                    else:
                        self.creation_message.text = ("The password need to have minimum 8 caracteres, a digit and a letter")
                else:
                    self.creation_message.text = ("The two password isnt the same")


class ShowCreatingTool(App):
    def build(self):
        Layout = CreateUserFunction()
        Layout.build()
        return Layout


if __name__ == '__main__':
    ShowCreatingTool().run()
