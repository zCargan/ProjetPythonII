from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Admin import Administrateur


class GiveRole(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.welcome()
        self.label_admin()
        self.input_admin()
        self.label_user()
        self.input_user()
        self.label_role()
        self.choose_role()
        self.validation_button()

    def welcome(self):
        self.label_welcome = Label(text="Welcome in the Admin Page", color=[1, 0.49, 0, 1],
                                   pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_welcome)

    # ----------------------------------------------------------- ADMIN SPACE -----------------------------------------------------------#

    def label_admin(self):
        self.label_id_admin = Label(text="Please enter your username", color=[1, 0.49, 0, 1],
                                    pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_id_admin)

    def input_admin(self):
        self.input_admin_user = TextInput(pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.input_admin_user)

    # ----------------------------------------------------------- USER SPACE -----------------------------------------------------------#

    def label_user(self):
        self.label_id_user_to_up = Label(text="Enter the name of the user to whom to give a role",
                                         color=[1, 0.49, 0, 1],
                                         pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_id_user_to_up)

    def input_user(self):
        self.input_user = TextInput(pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.input_user)

    # ----------------------------------------------------------- ROLE SPACE -----------------------------------------------------------#

    def label_role(self):
        self.user_roles_label = Label(text="New role of the user : ", color=[1, 0.49, 0, 1],
                                      pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.user_roles_label)

    def choose_role(self):
        self.option_list = Spinner(text="Choose the role",
                                   values=("Admin", "Modo", "User"),
                                   size_hint=(0.4, .17), pos_hint={'x': 0.3, 'y': 0.8},
                                   background_color=[1, 0.49, 0, 1])
        self.add_widget(self.option_list)

    def validation_button(self):
        self.button_of_validation = Button(text="Change role", size_hint=(.3, .02),
                                           pos_hint={'x': 0.35, 'y': 0.1}, color=[1, 1, 1, 1],
                                           background_color=[1, 0.49, 0, 1])
        self.button_of_validation.bind(on_press=self.validation)
        self.add_widget(self.button_of_validation)

    # ----------------------------------------------------------- Space Graphic -----------------------------------------------------------#

    def black_space(self):
        self.black = Label(size_hint=(.4, .1))
        self.add_widget(self.black)

    def validation(self, instance):
        self.admin = self.input_admin_user.text
        self.user = self.input_user.text
        self.role = self.option_list.text
        admin = Administrateur(self.admin)
        self.label_welcome.text = str(admin.manage_non_admin_role(self.user, self.role))
        admin.manage_non_admin_role(self.user, self.role)


class Window(App):
    def build(self):
        Layout = GiveRole()
        Layout.build()
        return Layout


if __name__ == '__main__':
    Window().run()
