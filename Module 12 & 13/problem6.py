# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:23:28 2026

@author: daria
"""

players = {}
file = open("players.txt", "r")
for line in file:
    data = line.split()
    name = data[0]
    avrg = float(data[1])
    players[name] = avrg
file.close()
def displayPlayers():
    print("Name", "Average")
    for name in players: 
        print(name, players[name])
displayPlayers()