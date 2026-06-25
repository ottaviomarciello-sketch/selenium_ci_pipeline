from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup




class Saluto(App):
    def build(self):
        mL = BoxLayout(orientation="vertical")

        et_nome = Label(text="Inserisci nome")
        mL.add_widget(et_nome)

        self.nome = TextInput(font_size=20)
        mL.add_widget(self.nome)

        bn_saluto = Button(text="Saluta")
        bn_saluto.bind(on_press=self.saluto_personalizzato)
        mL.add_widget(bn_saluto)

        return mL

    def saluto_personalizzato(self, instance):
        nome = self.nome.text.strip()

        if not nome:
            nome = "utente"

        pop_layout = BoxLayout(orientation="vertical")

        msg = f"Ciao {nome}, pronto per imparare Python oggi?"
        pop_layout.add_widget(Label(text=msg))

        bn_chiusura = Button(text="Chiudi")
        pop_layout.add_widget(bn_chiusura)

        pop = Popup(title="Messaggio", content=pop_layout, size_hint=(0.5, 0.5))

        bn_chiusura.bind(on_press=pop.dismiss)
        pop.open()