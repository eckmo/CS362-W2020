# -*- coding: utf-8 -*-
"""
Created on Thursday Jan 16 17:43:05 2020

@author: Morgan Eck
"""

import random
import testUtility
from collections import defaultdict

player_names = testUtility.getPlayerNames()
nV = testUtility.getNV(player_names)
# rather than a function call to the getNC(player_names) function
# in testUtility -- which would assign a number of Curse cards
# based on the number of players in the game in increments of 10 --
# this section hardcodes the value to 0, ensuring that no Curse
# cards are added to the game; this tests to see what happens with
# the game when 0 Curse cards are present
nC = 0
box = testUtility.createBoxes(nV)
supply_order = testUtility.createSO()
supply = testUtility.generateSupply(box, nV, nC, player_names)
trash = testUtility.getTrash()
players = testUtility.createPlayer(player_names)
testUtility.playGameFunction(supply, supply_order, players, trash)
testUtility.finalScoreFunction(players)
