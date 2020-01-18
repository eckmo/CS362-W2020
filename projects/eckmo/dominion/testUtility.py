# -*- coding: utf-8 -*-
"""
Created on Thursday Jan 16 17:43:05 2020

@author: Morgan Eck
"""

import Dominion
import random
from collections import defaultdict

# Get player names - the player names array is wrapped
# inside a function that returns the array
def getPlayerNames():
    player_names = ["Annie", "*Ben", "*Carla"]
    return player_names

# number of curses and victory cards - these generation
# statements are wrapped inside functions that return the
# nV and nC variables; the function receives the player_names
# array as parameter from our testDominion files
def getNV(player_names):
    if len(player_names) > 2:
        nV = 12
    else:
        nV = 8
    return nV
def getNC(player_names):
    nC = -10 + 10 * len(player_names)
    return nC

# Define box - creates a box based on a passed parameter
# Adapted from original box creation in that it was
# wrapped inside a function
def createBoxes(nV):
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()] * 10
    box["Smithy"] = [Dominion.Smithy()] * 10
    box["Laboratory"] = [Dominion.Laboratory()] * 10
    box["Village"] = [Dominion.Village()] * 10
    box["Festival"] = [Dominion.Festival()] * 10
    box["Market"] = [Dominion.Market()] * 10
    box["Chancellor"] = [Dominion.Chancellor()] * 10
    box["Workshop"] = [Dominion.Workshop()] * 10
    box["Moneylender"] = [Dominion.Moneylender()] * 10
    box["Chapel"] = [Dominion.Chapel()] * 10
    box["Cellar"] = [Dominion.Cellar()] * 10
    box["Remodel"] = [Dominion.Remodel()] * 10
    box["Adventurer"] = [Dominion.Adventurer()] * 10
    box["Feast"] = [Dominion.Feast()] * 10
    box["Mine"] = [Dominion.Mine()] * 10
    box["Library"] = [Dominion.Library()] * 10
    box["Gardens"] = [Dominion.Gardens()] * nV
    box["Moat"] = [Dominion.Moat()] * 10
    box["Council Room"] = [Dominion.Council_Room()] * 10
    box["Witch"] = [Dominion.Witch()] * 10
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
    box["Militia"] = [Dominion.Militia()] * 10
    box["Spy"] = [Dominion.Spy()] * 10
    box["Thief"] = [Dominion.Thief()] * 10
    box["Throne Room"] = [Dominion.Throne_Room()] * 10
    return box

# Define supply order - creates a supply order for the game
# Adapted from original supply order creation in that it was
# wrapped inside a function
def createSO():
    supply_order = {0: ['Curse', 'Copper'], 2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                    3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                    4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief',
                        'Throne Room'],
                    5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                    6: ['Gold', 'Adventurer'], 8: ['Province']}
    return supply_order

# Pick 10 cards from box to be in the supply.
# Wrap the commands in a function that takes a
# box as parameter and returns a random 10 cards
# as the supply; receives box, nV & nC from our test programs
def generateSupply(box, nV, nC, player_names):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list, [(k, box[k]) for k in random10])


# The supply always has these cards
# This part of the function takes the supply list
# created above and assigns values to the random
# 10 cards; these are then returned
    supply["Copper"] = [Dominion.Copper()] * (60 - len(player_names) * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * nV
    supply["Duchy"] = [Dominion.Duchy()] * nV
    supply["Province"] = [Dominion.Province()] * nV
    supply["Curse"] = [Dominion.Curse()] * nC
    return supply

# initialize the trash
# Wrapped in a function that returns the trash for use
# in other files
def getTrash():
    trash = []
    return trash

# Construct the Player objects
# This functionality is wrapped in a function that accepts
# player_names from testDominion files and returns a player
# object for use
def createPlayer(player_names):
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

# Play the game
# This functionality is wrapped within a function so
# that it may receive the necessary variables via
# parameters from our two testDominion files
def playGameFunction(supply, supply_order, players, trash):
    turn = 0
    while not Dominion.gameover(supply):
        turn += 1
        print("\r")
        for value in supply_order:
            print(value)
            for stack in supply_order[value]:
                if stack in supply:
                    print(stack, len(supply[stack]))
        print("\r")
        for player in players:
            print(player.name, player.calcpoints())
        print("\rStart of turn " + str(turn))
        for player in players:
            if not Dominion.gameover(supply):
                print("\r")
                player.turn(players, supply, trash)

# Final score
# This functionality is wrapped within a function so
# that necessary variables may be passed as parameters
# via our two testDominion files
def finalScoreFunction(players):
    dcs = Dominion.cardsummaries(players)
    vp = dcs.loc['VICTORY POINTS']
    vpmax = vp.max()
    winners = []
    for i in vp.index:
        if vp.loc[i] == vpmax:
            winners.append(i)
    if len(winners) > 1:
        winstring = ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0], 'wins!'])

    print("\nGAME OVER!!!\n" + winstring + "\n")
    print(dcs)