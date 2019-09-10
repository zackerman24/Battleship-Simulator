#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:12:40 2019

@author: Zackerman24
"""

import numpy as np
import game_setup as gs

"""There's probably a way of creating six separate lists for each letter
    and then combining them into one array. Look into this after?"""

base_array = np.array([['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
                       ['B1', 'B2', 'B3', 'B4', 'B5', 'B6'],
                       ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'], 
                       ['D1', 'D2', 'D3', 'D4', 'D5', 'D6'],
                       ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
                       ['F1', 'F2', 'F3', 'F4', 'F5', 'F6']])

player_one_ships_array = np.copy(base_array)
player_two_ships_array = np.copy(base_array)

print(player_one_ships_array)

battleship_coord = input(("\nEnter four adjacent coordinates for your battleship"
                         ", separated by a space: "))

battleship_coord = battleship_coord.split()
print(len(battleship_coord))

"""If Battleship_Coord has a length different than 4, re-do it"""

battleship_search = []

for coord in battleship_coord:
    spot = np.where(base_array == coord)
    place = list(zip(spot[0],spot[1]))
    battleship_search.append(place)

print(battleship_search)
print(battleship_search[0])

pair = battleship_search[0]

pair_2 = pair[0]

player_one_ships_array[pair_2[0],pair_2[1]] = 'X'

print(player_one_ships_array)

gs.create_battleship(base_array,player_one_ships_array)

"""
Ships will be represented in each player's array as X's
Each player will also have a 'targets' array, tracking their moves
When a player enters a move, it will reference the original array
    to identify the index location of the guess, and then search
    the opposing player's array at that spot to see if it has struck
"""