import json
import os
import shutil

path = "D:/Downloads/label"
path_dir = "D:/Workspace/labelset"
sum1 = 0

for root, dirs, files in os.walk(path):
    for di in dirs:
        if (di != "label"):
            for ro, d, fil in os.walk(os.path.join(root, di)):
                for f in fil:
                    if (f[-4:] == "json"):
                        sum1 += 1
                        # print("labelme_json_to_dataset \"" + os.path.join(ro, f) + "\" -o \"" + os.path.join(ro, f[:-5]) + '\"')
                        # os.system("mkdir \"" + os.path.join(ro, f[:-5]) + '\"')
                        os.system("labelme_json_to_dataset \"" + os.path.join(ro, f) + "\" -o \"" + os.path.join(ro, f[:-5]) + '\"')
print(sum1)