# Распознавание текста со скриншотов, сделанных прессом РП400.
# Спасибо разработчикам, сохранившим данные в виде скриншота.
# Используется библиотека pytesseract (https://pypi.org/project/pytesseract/) и pillow
# Ради распознавания кириллицы прикручен tesseract-ocr-rus

import os
import pytesseract
from PIL import Image
from datetime import datetime

SOURCE = '/opt/datasets/rp400/'
DATASET = '/opt/datasets/rp400/dataset.txt'
NUMBER = (31, 386, 198, 424)        # Координаты поля номера оси
OPERATOR = (574, 381, 743, 418)     # Координаты поля фамилии оператора

if __name__ == '__main__':
    press = []
    for i in range(2):
        cat = SOURCE + 'rp400-' + str(i + 1)
        print("Обработка каталога ", cat)
        files = os.listdir(cat)
        for x in files:
            fullname = cat + '/' + x     # Полное имя с путями, для вытаскивания даты следующим шагом
            string = datetime.fromtimestamp(os.path.getmtime(fullname)).strftime('%Y-%m-%d %H:%M:%S').split(' ')

            # Тащим pillow для подготовки изображения к OCR. Кропаем поле по заданным координатам.
            image = Image.open(fullname)
            cropped = image.crop(NUMBER)

            # Распознаём числовое поле с номером оси, если он указан. Обрезаем символ '\n'.
            # В опциях метода указываем белый список символов для повышения качества OCR.
            recognized = pytesseract.image_to_string(cropped, config='-c tessedit_char_whitelist=0123456789')
            axis = '' if recognized == '' else recognized.rstrip()

            # Распознаём текстовое поле с фамилией оператора, если она указана. Обрезаем символ '\n'.
            # В опциях метода указываем язык и параметр psm для одиночного слова.
            cropped = image.crop(OPERATOR)
            recognized = pytesseract.image_to_string(cropped, lang='rus', config='-c --psm=8')
            worker = '' if recognized == '' else recognized.rstrip()

            # Собираем список.
            string.append(axis)
            string.append(worker)
            # И в итоговый список списков.
            press.append(string)

    # Здесь не используем pandas. Потому что попробуй с пандами и сам увидишь.
    with open(DATASET, 'w') as dataset_file:
        rows = 0
        for w in press:
            dataset_file.write(f"{w}\n")
            rows += 1
        print(rows, 'строк')
