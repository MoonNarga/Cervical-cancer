import json
import os
import shutil

path = "D:/Workspace/labelset"
path_dir = "D:/Workspace/labelset"
sum1 = 0

for root, dirs, files in os.walk(path):
    for di in dirs:
        if (di != "labelset"):
            for ro, d, fil in os.walk(os.path.join(root, di)):
                for f in fil:
                    if (f[-4:] == "json" and f != "0000.json" and f[:3] != "fix"):
                        time = f[:4]
                        sum1 += 1
                        id = ro[22:]  
                        # print(time)

                        os.system("mkdir \"D:/Workspace/acetic/" + id + '\"')
                        os.system("labelme_json_to_dataset \"" + os.path.join(ro, f) + "\" -o " + "\"D:/Workspace/acetic/" + id + '/' + time + '\"')
print(sum1)