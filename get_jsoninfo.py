import json
from json import encoder
import os

path = "E:/labelset"

for root, dirs, files in os.walk(path):
    for f in files:
        if (f[-4:] == "json" and f[:3] != "fix"):
            fp = open(os.path.join(root, f), encoding="utf-8")
            js = json.load(fp)
            del js["imageData"]
            print(js)
