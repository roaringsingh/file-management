# Roaring Singh
# File Arrangement.py
# 28-12-2022
# 17:00

from PIL import Image
import pillow_heif
import math
import heapq
import copy
import os
from collections import defaultdict, OrderedDict


def HEICtoJPG(parent, child, flg=False):
    if not flg:
        return
    heif_file = pillow_heif.read_heif(os.path.join(parent, child))
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(os.path.join(os.path.split(parent)[0], 'jpg', ''.join(child.split('.')[:-1]) + ' conv.jpg'), "JPEG")
    print('Converted ' + child)


def arrangement(path, flg=False):
    for root, dirs, files in os.walk(path):
        print('Directory: ' + root)
        print('Subdirectory: ', *dirs)
        print('Files: ', *files)
        try:
            os.rmdir(root)
            print('Removed ' + root)
        except:
            pass
        for file in files:
            if file.split('.')[-1].lower() == 'heic':
                HEICtoJPG(root, file, flg)
            if os.path.split(root)[-1] == file.split('.')[-1]:
                continue
            os.renames(os.path.join(root, file), os.path.join(root, file.split('.')[-1], file))
            print('Moved ' + file)
        print('***')

path = input("Enter the absolute path of the folder:\n")
if 'y' == input('Convert HEIC to JPG?\n'):
    arrangement(path,True)
else:
    arrangement(path)
