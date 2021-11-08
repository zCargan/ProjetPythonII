from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CreateUserFunction(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.label_creation()

    def label_creation(self):
        self.creation_message = Label(text="Create your account")
        self.add_widget(self.creation_message)


class ShowCreatingTool(App):
    def build(self):
        Layout = CreateUserFunction()
        Layout.build()
        return Layout


if __name__ == '__main__':
    ShowCreatingTool().run()
