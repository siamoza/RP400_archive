# Фильтрация сырых датасетов с пресса 7, предварительно сформированных скриптом press7.py.
#
import pandas as pd

SOURCE = '/opt/datasets/rp400/dataset.txt'
FILTERED = '/opt/datasets/rp400/filtered.txt'

if __name__ == '__main__':
    # Зачистка датафреймов. Таблица 'press'.
    p = pd.read_csv(SOURCE, dtype=str, skipinitialspace=True, delimiter=',')
    p.columns = ["date", "time", "axis", "worker"]
    p_stat = "До зачистки " + str(len(p)) + " строк."
