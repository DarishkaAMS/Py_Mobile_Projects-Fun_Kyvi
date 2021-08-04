import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyFirstGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyFirstGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside_grid = GridLayout()
        self.inside_grid.cols = 2

        self.inside_grid.add_widget(Label(text="Your Firstname: "))
        self.firstname = TextInput(multiline=False)
        self.inside_grid.add_widget(self.firstname)

        self.inside_grid.add_widget(Label(text="Your Lastname: "))
        self.lastname = TextInput(multiline=False)
        self.inside_grid.add_widget(self.lastname)

        self.inside_grid.add_widget(Label(text="Your Email: "))
        self.email = TextInput(multiline=False)
        self.inside_grid.add_widget(self.email)

        self.inside_grid.add_widget(Label(text="Your Dream: "))
        self.dream = TextInput(multiline=False)
        self.inside_grid.add_widget(self.dream)

        self.add_widget(self.inside_grid)

        self.submit = Button(text="Send Me", font_size=40)
        self.submit.bind(on_press=self.press_button)
        self.add_widget(self.submit)

    def press_button(self, instance):
        # print("You have pressed me! :)")
        firstname = self.firstname.text
        lastname = self.lastname.text
        email = self.email.text
        dream = self.dream.text
        print(firstname, lastname, email, dream)
        self.firstname.text = ""
        self.lastname.text = ""
        self.email.text = ""
        self.dream.text = ""


class DarishkaAMSApp(App):
    def build(self):
        return MyFirstGrid()


if __name__ == "__main__":
    DarishkaAMSApp().run()
