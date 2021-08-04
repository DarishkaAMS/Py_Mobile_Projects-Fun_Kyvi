import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_up(self, touch):
        self.btn.opacity = 0.5
        print("Mouse UP", touch)

    def on_touch_down(self, touch):
        self.btn.opacity = 1
        print("Mouse DOWN", touch)

    def on_touch_move(self, touch):
        print("Mouse MOVE", touch)


class FourthApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    FourthApp().run()
