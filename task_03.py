import sys
from pathlib import Path

# Функція для парсингу рядків логу.
# приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами:
#  дата, час, рівень, повідомлення. Використовуйте методи рядків, як-от split(), для розділення рядка на частини.

def parse_log_line(line: str) -> dict:
    dict = {}
    data = line.split(' ')
    #print(data)
    date, time, level, *msg = data
    msg = ' '.join(msg).strip()
    dict = {'date': date, 'time' : time, 'level': level, 'msg': msg}
    #print(d)
    #print(dict)
    return dict

# Функція для завантаження логів з файлу.
# відкриває файл, читає кожен рядок і застосовує до нього функцію parse_log_line, зберігаючи результати у список.

def load_logs(file_path: str) -> list:
    l =[]
    with open(file_path, "r", encoding='utf-8') as fh:
        for line in fh:
            l.append(parse_log_line(line))
            #print(l)
        return l

# Функція для фільтрації логів за рівнем.
# Вона дозволить вам отримати всі записи логу для певного рівня логування.
def filter_logs_by_level(logs: list, level: str) -> list:
    print(f"Деталі логів для рівня '{level.upper()}':")
    #print(logs)
    for el in logs:
        #date, time, level, *msg = el
        #print(el)
        for key, value in el.items():
            if value == level.upper():
                print(el['date'] +' '+ el['time'] + ' - ' + el['msg'])

# Функція для підрахунку записів за рівнем логування.
# проходить по всіх записах і підраховує кількість записів для кожного рівня логування.
def count_logs_by_level(logs: list) -> dict:
    d = {}
    for el in logs:
        #print(el)
        for key,value in el.items():
            if key == 'level':
                if value in d:
                    d[value] += 1
                else:
                    d[value] = 1
    return d

# форматує та виводить результати підрахунку в читабельній формі.
#  Вона приймає результати виконання функції count_logs_by_level.

def display_log_counts(counts: dict):
    print(f'Рівень логування | Кількість')
    print(f"--------------------------------")
    for level, count in counts.items():
        print(f'{level:<16} | {count:^10}')
    
# Перевірка, чи передан скрипту абсолютний шлях до директоріЇ як параметр
if len(sys.argv) < 2:
    print('Please provide path')
    sys.exit()

# шлях до директорії як аргумент при запуску. Цей шлях вказує,
#  де знаходиться директорія, структуру якої потрібно відобразити.
file_path = Path(sys.argv[1])

# скрипт із додатковим аргументом
if len(sys.argv) > 2:
    file_path = Path(sys.argv[1])
    level = sys.argv[2]
    try:
        stat_info = load_logs(file_path)
        d = count_logs_by_level(stat_info)
        display_log_counts(d)
        filter_logs_by_level(stat_info, level)
    except FileNotFoundError:
        print("No file available.")

if len(sys.argv) == 2:
# види помилок, як-от відсутність файлу або помилки при його читанні.
    try:
        stat_info = load_logs(file_path)
        d = count_logs_by_level(stat_info)
        display_log_counts(d)

    except FileNotFoundError:
        print("No file available.")