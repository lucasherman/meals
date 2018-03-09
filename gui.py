from kivy.app import App
from kivy.uix.textinput import TextInput


class MealsApp(App):

    def build(self):
        return TextInput(text='Hello World')

MealsApp().run()