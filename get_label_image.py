import json
import os

path = "E:\labelset"
path_dir = "E:\labelset"
sum1 = 0

for root, dirs, files in os.walk(path):
    for di in dirs:
        if (di != "labelset"):
            for ro, d, fil in os.walk(os.path.join(root, di)):
                for f in fil:
                    if (f == "0000.json"):
                        sum1 += 1
                        id = ro[12:]                        
                        os.system("labelme_json_to_dataset \"" + os.path.join(ro, f) + "\" -o " + "\"E:/iodine/" + id + '\"')
print(sum1)