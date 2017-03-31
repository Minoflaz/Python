#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import random
import math

#Returns 1 for a win, 0 for a good guess of the case color and -1 for a loose
def gamble(case):

	win = -1
	rand = random.randrange(50)
	if case == rand:
		win = 1
	elif case%2 == rand%2:
		win = 0	

	return win


#Plays a game of casino which triples your bet in case of win, divides it by two when the color was good and you loose all your money when loosing 
def play():

	mise = verifInt("\nVeuillez indiquer la somme misée ($) : ")

	while mise>0:

		case = verifInt("\nVeuillez indiquer la case sur laquelle vous misez (0 à 49) : ")
		resultat = gamble(case)

		if resultat == 1:
			mise = mise * 3
			print("Vous avez trouvé la bonne case ! \n Vous gagnez deux fois la somme misée et vous disposez de {} $".format(mise))
		elif resultat == 0:
			mise = math.ceil(mise/2)
			print("Case misée de la même couleur que la bonne case ! \n Vous perdez que la moitié de votre mise et vous disposez de {} $".format(mise))
		else:
			mise = 0
			print("PERDU ! Vous perdez tout votre argent ! A bientot sous les ponts :/")

#Takes a display input message and returns the input when it is an integer 
def verifInt(message):

	cond = True

	while cond:
		try:
			sInput = input(message)
			sInput = int(sInput)
		except:	
			print("Entez un nombre")	
			continue
		else:
			cond = False
	return sInput


play()