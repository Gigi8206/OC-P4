class CreatePlayer:
    def display_menu(self):
        last_name = input("""Nom du joueur:\n> """)

        first_name = input("""Prénom du joueur:\n> """)

        birthday = self.get_user_entry(
            msg_display="Date de naissance (format DD-MM-YYYY):\n> ",
            msg_error="Veuillez entrer une date au format valide: DD-MM-YYYY",
            value_type="date",
        )
        print(f"Joueur {first_name} {last_name} créé.")

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birthday": birthday,
            "identifier": 0,
        }
