# -*- coding: utf-8 -*-
"""
Created on Thursday Jan 16 17:43:05 2020

@author: Morgan Eck
"""

import random
import testUtility
from collections import defaultdict

player_names = testUtility.getPlayerNames()
# rather than a function call to the getNV(player_names) function
# in testUtility -- which would assign a number of Victory cards
# based on the number of players in the game --
# this section hardcodes the value to 100, inflating the number of
# Victory cards to alter the performance of the game
nV = 100
nC = testUtility.getNC(player_names)
box = testUtility.createBoxes(nV)
supply_order = testUtility.createSO()
supply = testUtility.generateSupply(box, nV, nC, player_names)
trash = testUtility.getTrash()
players = testUtility.createPlayer(player_names)
testUtility.playGameFunction(supply, supply_order, players, trash)
testUtility.finalScoreFunction(players)
