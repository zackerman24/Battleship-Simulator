#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:44:53 2019

@author: Zackerman24
"""

"""Battleship, Cruiser, and Destroyer"""
"""For checking correct coord entry, could make sure entry is in
A - F and 1-6"""
"""Make sure coordinate entries are unique, not duplicative"""

import numpy as np

def create_battleship(game_array, player_array, player_placements):
    """Creates a user's 4-coordinate long battleship."""
    
    coordinates = input(("\nEnter four adjacent coordinates for your battleship"
                         ", separated by a space: "))
    
    split_coord = coordinates.split()
    
    while True:
        if len(split_coord) != 4:
            print("Invalid coordinate entry. Please try again.")
            coordinates = input(("\nEnter four adjacent coordinates"
                                 "for your battleship"
                                 ", separated only by a space: "))
            split_coord = coordinates.split()
            continue
        else:
            for coord in split_coord:
                if (coord in player_placements):
                    print("Coordinates taken. Please try again.")
                    coordinates = input(("\nEnter four adjacent coordinates"
                                 "for your battleship"
                                 ", separated only by a space: "))
                    split_coord = coordinates.split()
                    continue
                else:
                    break
    
    placements = []
    
    for coord in split_coord:
        raw_spot = np.where(game_array == coord)
        spot = list(zip(raw_spot[0],raw_spot[1]))
        placements.append(spot)
    
    for place in placements:
        print(place)
        place_1 = place[0]
        player_placements.append(player_array[place_1[0],place_1[1]])
        player_array[place_1[0],place_1[1]] = 'BS'
    
    print(player_array)