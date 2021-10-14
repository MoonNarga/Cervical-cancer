import json
import os

path = "E:\labelset"
path_dir = "E:\labelset"
sum = 0
for root, dirs, files in os.walk(path):
    for dirname in dirs:
        # s = 0
        for root, subdir, fil in os.walk(os.path.join(path, dirname)):
            print(len(fil))