#!/usr/bin/python3.4
# -*-coding:utf-8 -*


dico = lambda x,y:{'positionX':x,'positionY':y}	

def testParams(**params):
	if "lol" in params:
		print(params["lol"])

sList = [1,2,3,4]
sDico = {"lol":2,"lolz":3}

for key in sDico.keys():
	print(str(sDico[key]) + "\n")