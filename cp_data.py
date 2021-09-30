import json
import os

path = "E:\dataset"
path_dir = "E:\dataset\labelset"
sum = 0

for root, dirs, files in os.walk(path):
    for dirname in dirs:
        for ro, subdir, files_ in os.walk(os.path.join(root, dirname)):    