from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from identification import dic_password
from kivy.core.window import Window


class Identification(BoxLayout):
    def build(self):
        self.title = 'Identification'
        self.orientation = "vertical"
        self.label_id()
        self.inputUserName()
        self.inputPassWord()
        # self.labelPassword()
        self.button_psw_forget()
        self.button_identification()

    def label_id(self):
        self.username = Label(text="Identification", font_size=20, color=[0, 1, 0, 1],
                              pos_hint={'x': 0.35, 'y': 0}, size_hint=(.3, .03))
        self.add_widget(self.username)

    def inputUserName(self):
        self.inputUsername = TextInput(text="username", font_size=20, pos_hint={'x': .25, 'y': 0}, size_hint=(.5, .03))
        self.add_widget(self.inputUsername)

    # def labelPassword(self):
    #     self.password = Label(text="What's your password", font_size=30, color=[0, 1, 0, 1],
    #                         pos_hint={'x': 0, 'y': 0})
    #     self.add_widget(self.password)

    def inputPassWord(self):
        self.inputPassword = TextInput(text="Password", font_size=20, pos_hint={'x': .25, 'y': 0}, size_hint=(.5, .03))
        self.add_widget(self.inputPassword)

    def button_identification(self):
        self.confirmationButton = Button(text="Sign in", size_hint=(.2, .02),
                                         pos_hint={'x': .40, 'y': 0})
        self.confirmationButton.background_color = [0, 1, 0, 1]
        self.confirmationButton.bind(on_press=self.function1)
        self.add_widget(self.confirmationButton)

    def button_psw_forget(self):
        self.confirmationButton = Button(text="Password forget?", size_hint=(.2, .004),
                                         pos_hint={'x': 0.40, 'y': 0})
        self.confirmationButton.background_color = [0, 1, 0, 1]
        self.confirmationButton.bind(on_press=self.function1)
        self.add_widget(self.confirmationButton)

    def create_account(self):
        self.confirmationButton = Button(text="Not account", size_hint=(.2, .004),
                                         pos_hint={'x': 0.40, 'y': 0})
        self.confirmationButton.background_color = [0, 1, 0, 1]
        self.confirmationButton.bind(on_press=self.function1)
        self.add_widget(self.confirmationButton)

    def function1(self, instance):
        if self.inputUsername.text == "Lolo":
            instance.text = "Bravo"
            self.label_id.text = "Bravo!" + " le texte du bouton est : " + self.button_identification
        else:
            instance.text = "Perdu"
            self.label_id.text = "le texte du bouton est : " + self.button_identification


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
