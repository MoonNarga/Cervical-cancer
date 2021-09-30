import json
import os

path = "e:/dataset"
path_dir = "E:\dataset\labelset"
sum = 0
for root, dirs, files in os.walk(path):
    for dirname in dirs:
        if (dirname == "label"):
            for ro, di, fi in os.walk(os.path.join(root, dirname)):
                for fil in fi:
                    if (fil.endswith('.json')):
                        print(os.path.join(ro, fil))
                        fp = open(os.path.join(ro, fil), encoding="utf-8")
                        js = json.load(fp)
                        del js['imagePath']
                        del js['imageData']
                        fp = open(os.path.join(ro, ("fix_" + fil)), mode="w", encoding="utf-8")
                        json.dump(js, fp, ensure_ascii=False, indent=2)
                        print(type(js))
                        sum += 1

print(sum)