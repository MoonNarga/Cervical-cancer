import json
from json import encoder
import os

path = "E:/labelset"

for root, dirs, files in os.walk(path):
    for f in files:
        if (f[-4:] == "json" and f[:3] != "fix"):
            try:
                with open(os.path.join(root, f), 'r', encoding="utf-8") as fp:
                    content = fp.read()
                with open(os.path.join(root, f), 'w', encoding="gbk") as fp:
                    fp.write(content)
            except UnicodeDecodeError as e:
                pass