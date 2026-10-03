from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder 
from kivymouse import Mouse
import requests

Builder.load_string('''
<App>:
    BoxLayout:
        orientation: 'vertical'
        GridLayout:
            cols: 2
            spacing: 10
            padding: 20

            # Háttér, felirat, szöveg
            Label:
                text: 'CODEX AI'
                color: (1, 1, 1)  
            
            # Görgött szövegdölog
            ScrollView:
                size_hint_y: None
                height: 400

                BoxLayout:
                    orientation: 'vertical'
                    Label:
                        text: '' # Válaszok a szöveg boxol.
                    TextInput: 
                        multiline: False
                        text_size: (15, 5)  # size of text input

            # Küldemény gomb
            Button:
                text: 'KÜLDÉS'
                on_press: root.send_chat() # A gomb megnyomása után a chat funkciót hívjuk
    ''')


class App(App):
    def build(self):
        return self.root

# A chat api meghívása
def send_chat():  
    question = self.textinput.text
    response = requests.post('http://localhost:11434/api/chat', json={'question': question}) # a gemma2 modellel küldjük meg az adatokat 

    print(response.json()) # A kérések eredménye


if __name__ == "__main__":
    App().run()  # A Python program futtatásához