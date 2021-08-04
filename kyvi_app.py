import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class MySecondGrid(GridLayout):
    pass


class DarishkaAMSApp(App):
    def build(self):
        return MySecondGrid()


if __name__ == "__main__":
    DarishkaAMSApp().run()
