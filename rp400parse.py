# Распознавание текста на скриншотах.
# Спасибо разработчикам, сохранившим данные в виде скриншота
#
import os
import pytesseract
from PIL import Image
import pandas as pd
from datetime import datetime

SOURCE = '/opt/datasets/rp400/172.16.41.108/usbdisk/disk_a_1/screenshots'
DATASET1 = '/opt/datasets/rp400/dataset1.txt'
LEFT_X = 32
LEFT_Y = 388
RIGHT_X = 743
RIGHT_Y = 418

if __name__ == '__main__':
    files = os.listdir(SOURCE)
    for x in files:
        fullname = SOURCE + '/' + x
        string = datetime.fromtimestamp(os.path.getmtime(fullname)).strftime('%Y-%m-%d %H:%M:%S').split(' ')
        image = Image.open(fullname)
        image_cropped = image.crop((LEFT_X, LEFT_Y, RIGHT_X, RIGHT_Y))
        st = pytesseract.image_to_string(image_cropped, lang='rus').split(" ")
        print("Файл ", x, "распознана строка:", st)
        first = "null" if st[0] == "" else st[0]
        second = "null" if st[1] == "" else st[1]
        string.append(first)
        string.append(second)
        # string.append(st)
        string.append(x)
        # string = [line.rstrip() for line in string]

        print(string)
