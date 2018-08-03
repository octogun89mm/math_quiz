# Principal program #
from loadingbar import loading_bar
from os import system
from time import sleep
from GuiTerminal import GuiTerminal as gt
from EquationGenerator import EquationGenerator as eg
from User import User

system("clear")

user_name = input("Veuillez entrer votre nom complet : ")

first_name, last_name = user_name.split(" ")

u1 = User(first_name,last_name)

system("clear")

gt.greeting(u1.get_first_name())
loading_bar()
