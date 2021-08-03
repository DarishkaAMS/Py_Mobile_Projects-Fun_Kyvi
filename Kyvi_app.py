import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyFirstApp(App):
    def build(self):
        return Label(text="DarishkaAMS")


if __name__ == "__main__":
    MyFirstApp().run()
