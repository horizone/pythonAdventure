#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import string
gameMap = [
{'desc':"Du står i ett fint Vardagsrum, Norrut finns en hall, österut ligger ryssland", 'n':1, 'o': 3, 'v': -1, 'game': 'ongoing'},
{'desc':"Du står i en smal hall, söderut finns ett vardagsrum och västerut en flygterminal",'s':0, 'v': 2, 'game': 'ongoing'},
{'desc':"Du står i en flygterminal, österut finns en hall.", 'o':1, 'game': 'ongoing' },
{'desc':"Ryssland. Nu är du i himlen. Du har faktist vunnit spelet.", 'game': 'complete'},
]
playerLocation = 0

##loop start
while 1:
    print (gameMap[playerLocation]['desc'])
    if gameMap[playerLocation]['game'] == "complete":
        print ("Grattis, Du klarade spelet")
        exit()
    command = input('Vart vill du gå? ')
    if command == "n":
        playerLocation = gameMap[playerLocation]['n']
    if command == "s":
        playerLocation = gameMap[playerLocation]['s']
    if command == "v":
        if gameMap[playerLocation]['v'] == -1:
            print ("Du kan inte gå in i väggen")
        else:
            playerLocation = gameMap[playerLocation]['v']
    if command == "o":
        playerLocation = gameMap[playerLocation]['o']
