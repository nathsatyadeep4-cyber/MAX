import os
import json
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import platform

class MAXAI(App):
    def build(self):
        self.title = "MAX AI"
        root = BoxLayout(orientation="vertical", padding=15, spacing=12)

        root.add_widget(Label(
            text="[b]MAX AI[/b]\nYour Personal AI Assistant",
            markup=True, font_size="28sp", size_hint_y=0.2
        ))

        self.output = Label(
            text="Hello! I am MAX. How can I help you?",
            halign="center", valign="middle"
        )
        self.output.bind(size=lambda obj, size: setattr(
            obj, "text_size", size
        ))
        root.add_widget(self.output)

        self.command = TextInput(
            hint_text="Type your command...",
            multiline=False, size_hint_y=0.12
        )
        root.add_widget(self.command)

        buttons = [
            ("Run Command", self.run_command),
            ("Open Google", lambda *_: self.open_url(
                "https://www.google.com")),
            ("Open YouTube", lambda *_: self.open_url(
                "https://www.youtube.com")),
            ("About MAX", lambda *_: self.about())
        ]

        for title, callback in buttons:
            button = Button(text=title, size_hint_y=0.12)
            button.bind(on_release=callback)
            root.add_widget(button)

        return root

    def run_command(self, *_):
        command = self.command.text.strip().lower()

        if not command:
            self.output.text = "Please type a command first."
        elif "hello" in command or "hi" in command:
            self.output.text = "Hello! MAX is ready."
        elif "time" in command:
            from datetime import datetime
            self.output.text = datetime.now().strftime("%I:%M %p")
        elif "google" in command:
            self.open_url("https://www.google.com")
        elif "youtube" in command:
            self.open_url("https://www.youtube.com")
        elif "help" in command:
            self.output.text = (
                "Try: hello, time, google, youtube, help"
            )
        else:
            self.output.text = (
                "Command not recognised. Type 'help' for commands."
            )

    def open_url(self, url):
        try:
            webbrowser.open(url)
            self.output.text = "Opening " + url
        except Exception as error:
            self.output.text = "Could not open link: " + str(error)

    def about(self):
        self.output.text = (
            "MAX AI\nPersonal assistant prototype\n"
            "More features require additional implementation."
        )

if __name__ == "__main__":
    MAXAI().run()
