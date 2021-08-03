import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class ChildApp(GridLayout):

    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 5

        self.add_widget(Label(text='User Name'))
        self.user_name = TextInput()
        self.add_widget(self.user_name)

        self.add_widget(Label(text='User Score'))
        self.user_score = TextInput()
        self.add_widget(self.user_score)

        self.add_widget(Label(text='User Gender'))
        self.user_gender = TextInput()
        self.add_widget(self.user_gender)


class ParentApp(App):

    def build(self):
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()