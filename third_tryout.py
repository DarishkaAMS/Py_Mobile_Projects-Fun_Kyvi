import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class ThirdApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    ThirdApp().run()
