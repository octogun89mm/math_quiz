class GuiTerminal:
    """
    A class that contains multiple printing methods
    """


    def print_menu_level():
        """
        Print the options for the level
        """
        print("1. Facile ..... (1 à 10)")
        print("2. Moyen ...... (10 à 20) ")
        print("3. Difficile .. (20 à 30)")
        print("4. Aide")
        print("5. Revenir au menu principal")

    def print_main_menu():
        """
        Print the options for the main menu
        """
        print("1. Nouvelle partie")
        print("2. Changer d'utilisateur")
        print("3. Quitter")

    def choose_user_menu(*args):
        """
        Forms a visual list of all the users
        by taking the users as arguments (strings)
        """
        i = 1
        for user in args:
            print(i, " " + user, sep=".")
            i += 1

    def print_equa(equa):
        """
        Print an equation (string)
        """
        print(equa)

    def print_answer(answer):
        """
        Print the correct answer
        """
        print("La réponse était {}.".format(answer))

    def greeting(username):
        """
        Print a greeting followed by the username
        """
        print("Bonjour {} !!!".format(username))
