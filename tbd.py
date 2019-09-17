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
player_one_placements = []
player_two_placements = []

print("\nAt any point in play, enter 'Exit' to exit the game.")

print("\nPlayer One select first. Place coordinates on your map.")
print(player_one_ships_array)
gs.create_ships(base_array,player_one_ships_array,player_one_placements)

print("\nPlayer Two now selects. Place coordinates on your map.")
print(player_two_ships_array)
gs.create_ships(base_array,player_two_ships_array,player_two_placements)



"""
Ships will be represented in each player's array as X's
Each player will also have a 'targets' array, tracking their moves
When a player enters a move, it will reference the original array
    to identify the index location of the guess, and then search
    the opposing player's array at that spot to see if it has struck
"""