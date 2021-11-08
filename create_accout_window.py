from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CreateUserFunction(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.label_creation()
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

    def input_username(self):
        self.username_input = TextInput(text="What's your username?", font_size=20, size_hint=(.4, .4),
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
        self.add_widget(self.confirmaccountcreation)


class ShowCreatingTool(App):
    def build(self):
        Layout = CreateUserFunction()
        Layout.build()
        return Layout


if __name__ == '__main__':
    ShowCreatingTool().run()
