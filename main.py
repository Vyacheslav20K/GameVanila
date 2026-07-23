import socks
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from telethon import TelegramClient

# ТЕМА: Фиолетовый фон (#0f081d)
Window.clearcolor = (0.06, 0.03, 0.11, 1)

REAL_API_ID = 2040
REAL_API_HASH = "b18441a1ed607e10e39051a9e961917f"

# Встроенный прокси SOCKS5
PROXY_TYPE = socks.SOCKS5
PROXY_IP = "185.199.229.156"
PROXY_PORT = 7492

class GameVanilaUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 15

        self.add_widget(Label(
            text="★ GameVanila Client ★",
            font_size='26sp',
            bold=True,
            color=(0.66, 0.33, 0.97, 1)
        ))

        self.phone_input = TextInput(
            hint_text="Номер телефона (+7...)",
            multiline=False,
            background_color=(0.15, 0.07, 0.26, 1),
            foreground_color=(0.91, 0.84, 1, 1),
            hint_text_color=(0.5, 0.4, 0.7, 1)
        )
        self.add_widget(self.phone_input)

        self.code_input = TextInput(
            hint_text="Код из Telegram",
            multiline=False,
            background_color=(0.15, 0.07, 0.26, 1),
            foreground_color=(0.91, 0.84, 1, 1),
            hint_text_color=(0.5, 0.4, 0.7, 1)
        )
        self.add_widget(self.code_input)

        self.login_btn = Button(
            text="ВОЙТИ В TELEGRAM",
            background_normal='',
            background_color=(0.54, 0.36, 0.96, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        self.add_widget(self.login_btn)

class GameVanilaApp(App):
    def build(self):
        self.title = "GameVanila"
        return GameVanilaUI()

if __name__ == "__main__":
    client = TelegramClient(
        'gamevanila_session',
        REAL_API_ID,
        REAL_API_HASH,
        proxy=(PROXY_TYPE, PROXY_IP, PROXY_PORT)
    )
    GameVanilaApp().run()

