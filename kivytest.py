from kivy.app import App
from kivy.uix.button import Button

class TetsApp(App):
    def build(self):
        return Button(text="Hello World one!")

if __name__ == "__main__":
    TetsApp().run()