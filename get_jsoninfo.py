import json5
fp = open('E:/dataset/202011/02 5945555/label/01.json')
js = json5.load(fp)
d = js["shapes"]
for p in d:
    print(p["label"], p["points"], type(p["points"]), '\n')
