import json
from json import encoder
import os

path = "D:/Workspace/labelset"

for root, dirs, files in os.walk(path):
    for f in files:
        if (f[-4:] == "json" and f[:3] != "fix"):
            try:
                fp = open(os.path.join(root, f), 'r', encoding="utf-8")
                content = json.load(fp)
                # print(content["shapes"])
                fp = open(os.path.join(root, f), 'w', encoding="gbk")
                json.dump(content, fp, indent=2, ensure_ascii=False)
            except UnicodeDecodeError as e:
                pass