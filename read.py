from PIL import Image
import json
import os

path = "D:\Workspace\labelset"
im = []
label = []
for root, dirs, files in os.walk(path):
    for sdir in dirs:
        for ro, ssdir, fil in  os.walk(os.path.join(root, sdir)):
            for f in fil:
                if (f[-4:] == ".jpg"):
                    fname = f[:-4]
                    print(fname)
                    # temp_im = Image.open()