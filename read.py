from PIL import Image
import json5

fp = open('E:/dataset/202011/02 5945555/label/0100.json')
js = json5.load(fp)
im = js["imageData"]
print(im)
# im = Image.frombytes(mode="RGB", size=[1440,1080], data=bytes(im, encoding="utf-8"), decoder_name="raw")
# im.show()
