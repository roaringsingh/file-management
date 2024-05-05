# Roaring Singh
# Image Duplicacy.py
# 30-12-2022
# 01:00

import math
import heapq
import copy
import os
import cv2
import numpy as np
from collections import defaultdict, OrderedDict

path = input("Enter the path of the folder containing only images:\n")


def dhash(image, hashSize=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


hashes = {}
for file in os.listdir(path):
    imagePath = os.path.join(path, file)
    print(imagePath)
    # load the input image and compute the hash
    image = cv2.imread(imagePath)
    h = dhash(image)
    # grab all image paths with that hash, add the current image
    # path to it, and store the list back in the hashes dictionary
    p = hashes.get(h, [])
    p.append(imagePath)
    hashes[h] = p

for (h, hashedPaths) in hashes.items():
    # check to see if there is more than one image with the same hash
    if len(hashedPaths) > 1:
        # initialize a montage to store all images with the same hash
        montage = None
        # loop over all image paths with the same hash
        for p in hashedPaths:
            # load the input image and resize it to a fixed width
            # and heightG
            image = cv2.imread(p)
            image = cv2.resize(image, (250, 250))
            # if our montage is None, initialize it
            if montage is None:
                montage = image
            # otherwise, horizontally stack the images
            else:
                montage = np.hstack([montage, image])
        # show the montage for the hash
        print("[INFO] hash: {}".format(h))
        cv2.imshow("Montage", montage)
        cv2.waitKey(1000)
        res = input('Delete ?')
        if res == 'y':
            for p in hashedPaths[1:]:
                os.remove(p)
                print('removed',p)
