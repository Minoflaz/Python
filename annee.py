#!/usr/bin/python3.4
# -*-coding:utf-8 -*
def bissextile():
	while 1==1:
		annee =  input("\nVeuillez entrez une annee : ")

		try:
			annee = int(annee)
		except:
			continue

		if annee%4 == 0:
			print("\nCeci est une année bissextile")
		else:
			print("ceci n'est pas une annee bissextile")

square =  lambda x: x*x
bissextile()