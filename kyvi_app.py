import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class MySecondGrid(GridLayout):
    first_name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)
    dream = ObjectProperty(None)

    def press_btn(self):
        print("First name: ", self.first_name.text)
        print("Last name: ", self.last_name.text)
        print("Email: ", self.email.text)
        print("Dream: ", self.dream.text)
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""
        self.dream.text = ""


class DarishkaAMSApp(App):
    def build(self):
        return MySecondGrid()


if __name__ == "__main__":
    DarishkaAMSApp().run()
