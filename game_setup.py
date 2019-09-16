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
    
    coordinates = input(("\nEnter four adjacent coordinates for your Battleship"
                         ", separated by a space: "))
    
    split_coord = coordinates.split()
    
    while True:
        if coordinates == "Exit":
            exit()
        elif len(split_coord) != 4:
            print("Invalid coordinate entry. Please try again.")
            coordinates = input(("\nEnter four adjacent coordinates"
                                 "for your Battleship"
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
        place_1 = place[0]
        player_placements.append(player_array[place_1[0],place_1[1]])
        player_array[place_1[0],place_1[1]] = 'BS'
    
    print(player_array)
    
def create_cruiser(game_array, player_array, player_placements):
    """Creates a user's 3-coordinate long cruiser."""
    
    coordinates = input(("\nEnter three adjacent coordinates for your Cruiser"
                         ", separated by a space: "))
    
    split_coord = coordinates.split()
    
    while True:
        if coordinates == "Exit":
            exit()
        elif len(split_coord) != 3:
            print("Invalid coordinate entry. Please try again.")
            coordinates = input(("\nEnter three adjacent coordinates"
                                 "for your Cruiser"
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
        place_1 = place[0]
        player_placements.append(player_array[place_1[0],place_1[1]])
        player_array[place_1[0],place_1[1]] = 'CR'
    
    print(player_array)

def create_destroyer(game_array, player_array, player_placements):
    """Creates a user's 2-coordinate long cruiser."""
    
    coordinates = input(("\nEnter two adjacent coordinates for your Destroyer"
                         ", separated by a space: "))
    
    split_coord = coordinates.split()
    
    while True:
        if coordinates == "Exit":
            exit()
        elif len(split_coord) != 2:
            print("Invalid coordinate entry. Please try again.")
            coordinates = input(("\nEnter two adjacent coordinates"
                                 "for your Destroyer"
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
        place_1 = place[0]
        player_placements.append(player_array[place_1[0],place_1[1]])
        player_array[place_1[0],place_1[1]] = 'DT'
    
    print(player_array)

def create_ships(game_array, player_array, player_placements):
    """Function to create all three of a players ships."""
    
    create_battleship(game_array, player_array, player_placements)
    create_cruiser(game_array, player_array, player_placements)
    create_destroyer(game_array, player_array, player_placements)