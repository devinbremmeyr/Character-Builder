# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:24:35 2018

@author: Devin
"""

import random
TraitsFile = open("Traits.txt","r")

TraitsList = TraitsFile.readlines()

print "Behavior: " + TraitsList[random.randint(0,TraitsList.__len__()-1)]

TraitsFile.close()

TraitsFile = open("Emotions.txt","r")

TraitsList = TraitsFile.readlines()

print "Emotion: " + TraitsList[random.randint(0,TraitsList.__len__()-1)]

TraitsFile.close()

TraitsFile = open("Appearance.txt","r")

TraitsList = TraitsFile.readlines()

print "Appearance: " + TraitsList[random.randint(0,TraitsList.__len__()-1)]

TraitsFile.close()

print "STR:" + str(random.randint(1,18))
print "DEX:" + str(random.randint(1,18))
print "CON:" + str(random.randint(1,18))
print "INT:" + str(random.randint(1,18))
print "WIS:" + str(random.randint(1,18))
print "CHA:" + str(random.randint(1,18))

raw_input('Press Enter to Exit')