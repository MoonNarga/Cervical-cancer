import json
import os

path = "e:/dataset"
sum = 0

for root, dirs, files in os.walk(path):
    for dirname in dirs:
        if (dirname == "label"):
            for ro, di, fi in os.walk(os.path.join(root, dirname)):
                for fil in fi:
                    if ("fix" in fil):
                        os.remove(os.path.join(ro, fil))