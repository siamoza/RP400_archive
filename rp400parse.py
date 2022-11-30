# Распознавание текста на скриншотах.
# Спасибо разработчикам, сохранившим данные в виде скриншота
#
import os
import pytesseract
from PIL import Image
import pandas as pd
from datetime import datetime

SOURCE = '/opt/datasets/rp400'
DATASET = '/opt/datasets/rp400/ocr.txt'
LEFT_X = 32
LEFT_Y = 388
RIGHT_X = 738
RIGHT_Y = 419

if __name__ == '__main__':
    files = os.listdir(SOURCE)
    for x in files:
        fullname = SOURCE + '/' + x
        string = datetime.fromtimestamp(os.path.getmtime(fullname)).strftime('%Y-%m-%d %H:%M:%S').split(' ')
        image = Image.open(fullname)
        image_cropped = image.crop((LEFT_X, LEFT_Y, RIGHT_X, RIGHT_Y))
        st = pytesseract.image_to_string(image_cropped).split(" ")
        string.append(st[0])
        string.append(st[1])
        string.append(x)
        string = [line.rstrip() for line in string]

        print(string)
