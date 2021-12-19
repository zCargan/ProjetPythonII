from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from function import manage_roles, determine_all_role, search_user_role


class GiveRole(BoxLayout):
    def build(self):
        self.orientation = "vertical"
        self.welcome()
        self.id_admin()
        self.admin_user()
        self.id_user_to_up()
        self.user()
        self.button_search_user()
        self.role_from_user()
        self.list_role()
        self.role()
        self.list_option_role()
        self.validation_button()

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

    def id_user_to_up(self):
        self.label_id_user_to_up = Label(text="Enter the name of the user to whom to give a role", color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_id_user_to_up)

    def user(self):
        self.input_user = TextInput(pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.input_user)

    def button_search_user(self):
        self.button_search_username = Button(text="Search user", size_hint=(.3, .02),
                                             pos_hint={'x': 0.35, 'y' :0.1}, color=[1, 1, 1, 1], background_color=[0.59,0.239,0.89,1])
        self.button_search_username.bind(on_press=self.search_role_user)
        self.add_widget(self.button_search_username)


    def role_from_user(self):
        self.user_roles_label = Label(text="This is the role(s) that the user already has", color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.user_roles_label)

    def id_role(self):
        self.label_id_role = Label(text="Enter the name of the role you want to give", color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_id_role)

    def list_role(self):
        self.label_list_role = Label(text="Enter the name of the user to whom to give a role \n You can choose one if this :  " + str(determine_all_role()), color=[0.59, 0.239, 0.89, 1],
                                     pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.label_list_role)

    def role(self):
        self.input_role = TextInput(pos_hint={'x': 0.25, 'y': 0.9}, size_hint=(.5, .01))
        self.add_widget(self.input_role)

    def list_option_role(self):
        self.option_list = Spinner(text="Choose do remove or add",
                                   values=("Add role", "Remove role"),
                                   size_hint=(0.4, .01), pos_hint={'x': 0.3, 'y': 0.8}, background_color=[0.59,0.239,0.89,1])
        self.add_widget(self.option_list)


    def validation_button(self):
        self.button_of_validation = Button(text="Give role", size_hint=(.3, .02),
                                             pos_hint={'x': 0.35, 'y' :0.1}, color=[1, 1, 1, 1], background_color=[0.59,0.239,0.89,1])
        self.button_of_validation.bind(on_press=self.give_role)
        self.add_widget(self.button_of_validation)

    # ----------------------------------------------------------- Space Graphic -----------------------------------------------------------#

    def black_space(self):
        self.black = Label(size_hint=(.4, .1))
        self.add_widget(self.black)


    def search_role_user(self, instance):
        self.user_roles_label.text = "This is the role(s) that the user already has " + str(search_user_role(self.input_admin_user.text, self.input_user.text))


    def give_role(self, instance):
        admin = self.input_admin_user.text
        user = self.input_user.text
        role = self.input_role.text.upper()
        add_remove = self.option_list.text
        response = manage_roles(admin, user, add_remove, role)
        self.label_welcome.text = str(response)





class Window(App):
    def build(self):
        Layout = GiveRole()
        Layout.build()
        return Layout


if __name__ == '__main__':
    Window().run()
