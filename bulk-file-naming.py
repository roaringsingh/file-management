# Roaring Singh
# File Naming.py
# 29-11-2022
# 19:00

import math
import heapq
import copy
import os
from collections import defaultdict, OrderedDict


def extension(address):
    for file in os.listdir(address):
        os.rename(address + file, address + file + '.mkv')


def name(address):
    for file in os.listdir(address):
        print(file)
        new = file.split()
        print(new)
        # os.rename(address + file, address + " ".join(new))


path = "D:/Entertainment/Anime"
# Add the folder name in format '/name/'
folder = "//"
name(path + folder)
# extension(path + folder)
