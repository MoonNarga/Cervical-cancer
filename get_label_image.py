import json5
import os

path = "e:/dataset"
sum = 0
for root, dirs, files in os.walk(path):
    for dirname in dirs:
        if (dirname == "label"):
            for ro, di, fi in os.walk(os.path.join(root, dirname)):
                for fil in fi:
                    if (fil.endswith('.json')):
                        print(os.path.join(ro, fil))
                        fp = open(os.path.join(ro, fil))
                        js = json5.load(fp)
                        print(type(js))
                        fp.close()