import json
import os
import shutil

path = "D:\Workspace\dataset"
path_dir = "D:\Workspace\dataset\labelset"
sum = 0
for root, dirs, files in os.walk(path):
    for fil in files:
        if (fil == "0100.json"):
            sum += 1
            print(sum)
            # for ro, subdir, fi in os.walk(root):
            #     for f in fi:
            #         # print(os.path.join(ro, f), "   ", os.path.join(path_dir, ro[28:-6], f))
            #         shutil.copy(os.path.join(ro, f), os.path.join(path_dir, ro[28:-6], f))
            # os.mkdir(os.path.join(path_dir, root[28:-6]))
            # shutil.copy("", os.path.join(path_dir, root[28:-6]))
            
        # if (dirname == "label"):
        #     for ro, di, fi in os.walk(os.path.join(root, dirname)):
        #         for fil in fi:
        #             if (fil.endswith('.json')):
        #                 print(os.path.join(ro, fil))
        #                 fp = open(os.path.join(ro, fil), encoding="utf-8")
        #                 js = json.load(fp)
        #                 del js['imagePath']
        #                 del js['imageData']
        #                 fp = open(os.path.join(ro, ("fix_" + fil)), mode="w", encoding="utf-8")
        #                 json.dump(js, fp, ensure_ascii=False, indent=2)
        #                 print(type(js))
        #                 sum += 1

print(sum)