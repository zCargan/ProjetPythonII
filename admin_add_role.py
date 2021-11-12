from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from function import determine_all_role, modify_role
from function import manage_roles, determine_all_role


class AddRole(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.welcome()
        self.warning()
        self.id_admin()
        self.admin_user()
        self.list_option_role()
        self.roles_choice()
        self.role_choosen()
        self.apply_modification()

    def welcome(self):
        self.label_welcome = Label(text="Welcome in the Admin Page", color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_welcome)

    def warning(self):
        self.label_warning = Label(text="If you are not a admin, you can not do everything", color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_warning)

    def id_admin(self):
        self.label_id_admin = Label(text="Please enter your username", color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_id_admin)

    def admin_user(self):
        self.input_admin_user = TextInput(pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.input_admin_user)

    def list_option_role(self):
        self.option_list = Spinner(text="Choose do remove or add",
                                   values=("Add role", "Remove role"),
                                   size_hint=(0.4, .01), pos_hint={'x': 0.3, 'y': 0.8}, background_color=[0.59,0.239,0.89,1])
        self.add_widget(self.option_list)

    def roles_choice(self):
        self.label_role_chosen = Label(text="Choose the role to remove, you can choose betwenn :   " + str(determine_all_role()), color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_role_chosen)

    def role_choosen(self):
        self.input_role_choosen = TextInput(pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.input_role_choosen)

    def apply_modification(self):
        self.button_apply = Button(text="Apply", size_hint=(.3, .02),
                                             pos_hint={'x': 0.35, 'y' :0.1}, color=[1, 1, 1, 1], background_color=[0.59,0.239,0.89,1])
        self.button_apply.bind(on_press=self.modify_role)
        self.add_widget(self.button_apply)

    def modify_role(self, instance):
        user = self.input_admin_user.text
        choice = self.option_list.text
        role = self.input_role_choosen.text
        message = modify_role(user, choice, role)
        self.label_role_chosen.text = ("The new role list :  " + str(message) + "  " + str(determine_all_role()))
        list_roles = determine_all_role()
        self.label_welcome.text = str(list_roles)

class WindowTwo(App):
    def build(self):
        Layout = AddRole()
        Layout.build()
        return Layout


if __name__ == '__main__':
    WindowTwo().run()