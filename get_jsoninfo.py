import json
from json import encoder
import os

path = "D:/Workspace/labelset"

for root, dirs, files in os.walk(path):
    for f in files:
        if (f[-4:] == "json" and f[:3] != "fix"):
            try:
                fp = open(os.path.join(root, f), 'r', encoding="gbk")
                content = json.load(fp)
                content["imagePath"] = f[:4] + ".jpg"
                # print(f, content["imagePath"])
                for lab in content["shapes"]:
                    if (lab["label"] == "宫颈CA"):
                        lab["label"] = "HSIL+"
                    elif (lab["label"] == "HSIL"):
                        lab["label"] = "HSIL+"
                    elif (lab["label"] == "CIN 2"):
                        lab["label"] = "HSIL+"
                    elif (lab["label"] == "CIN 1"):
                        lab["label"] = "LSIL"
                # for lab in content["shapes"]:
                #     print(lab["label"])
                fp = open(os.path.join(root, f), 'w', encoding="gbk")
                json.dump(content, fp, indent=2, ensure_ascii=False)
            except UnicodeDecodeError as e:
                pass