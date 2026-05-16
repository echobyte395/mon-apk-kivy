from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Morpion(App):

    def build(self):

        self.joueur = "X"
        self.grille = [""] * 9
        self.boutons = []

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.label = Label(
            text=f"Tour du joueur : {self.joueur}",
            font_size=40,
            size_hint=(1, 0.15)
        )

        self.layout.add_widget(self.label)

        grille_layout = GridLayout(cols=3, spacing=10)

        for i in range(9):
            bouton = Button(
                text="",
                font_size=80,
                background_color=(0.2, 0.2, 0.2, 1)
            )

            bouton.bind(on_press=lambda instance, i=i: self.cliquer(i))

            self.boutons.append(bouton)
            grille_layout.add_widget(bouton)

        self.layout.add_widget(grille_layout)

        reset = Button(
            text="Recommencer",
            font_size=30,
            size_hint=(1, 0.15)
        )

        reset.bind(on_press=lambda x: self.recommencer())

        self.layout.add_widget(reset)

        return self.layout

    def verifier_victoire(self):

        combinaisons = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

        for a, b, c in combinaisons:
            if self.grille[a] == self.grille[b] == self.grille[c] != "":
                return self.grille[a]

        if "" not in self.grille:
            return "Égalité"

        return None

    def cliquer(self, index):

        if self.grille[index] == "":

            self.grille[index] = self.joueur
            self.boutons[index].text = self.joueur

            resultat = self.verifier_victoire()

            if resultat:

                if resultat == "Égalité":
                    texte = "Match nul !"
                else:
                    texte = f"Le joueur {resultat} a gagné !"

                popup = Popup(
                    title="Fin",
                    content=Label(text=texte),
                    size_hint=(0.7, 0.4)
                )

                popup.open()

                self.recommencer()

            else:
                self.joueur = "O" if self.joueur == "X" else "X"
                self.label.text = f"Tour du joueur : {self.joueur}"

    def recommencer(self):

        self.joueur = "X"
        self.grille = [""] * 9

        for bouton in self.boutons:
            bouton.text = ""

        self.label.text = f"Tour du joueur : {self.joueur}"

Morpion().run()