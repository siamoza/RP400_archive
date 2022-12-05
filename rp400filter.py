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

    p['worker'].replace(to_replace=r'\'', value='', regex=True, inplace=True)
    p['date'].replace(to_replace=r'^\[', value='', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'\]$', value='', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'БОЕС', value='БОЕВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'БУЛГАК.*', value='БУЛГАКОВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ЮОЕВ', value='БОЕВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ВОРОНК.*', value='ВОРОНКОВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'КУЗНЕЦ.*', value='КУЗНЕЦОВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'КУКШИН.*', value='КУКШИНОВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ЛУНЕВ', value='ЛУНЁВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ТИБЕКИ.*', value='ТИБЕКИН', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ХОРХОР.*', value='ХОРХОРДИН', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ЧЕРНИК.*', value='ЧЕРНИКОВ', regex=True, inplace=True)
    p['worker'].replace(to_replace=r'ШКАБАР.*', value='ШКАБАРНЯ', regex=True, inplace=True)

    p.sort_values('date')
    p.to_csv(FILTERED, index=False)
