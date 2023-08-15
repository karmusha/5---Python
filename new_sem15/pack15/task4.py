# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# Верните дату в текущем году, соответствующую этому тексту.
# Логируйте ошибки, если текст не соответсвует формату.
# Логируйте кортеж именованного типа с атрибутами, соответствующими дате, если дата существует.

import logging
import re

FORMAT = '{asctime} - {levelname:<5} - {funcName} -> {lineno}: {msg}'

logging.basicConfig(filename='sem15_4.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    format=FORMAT,
                    style='{')
logger = logging.getLogger('__name__')


def get_date(text=None) -> None:
    if text == None:
        text = input('Input: ')
    try:
        num, week_day, month = text.split()
    except ValueError:
        logger.info(f'{num, week_day, month}')
    finally:
        xnum = re.findall('\d+', num)[0]
        xweek_day = week_day[:3]
        xmonth = month[:2]
        print(xnum, xweek_day, xmonth)

    
days = {'пон': 1,
        'вто': 2,
        'сре': 3,
        'чет': 4,
        'пят': 5,
        'суб': 6,
        'вос': 7,}

months = {'янв': 1,
        'фев': 2,
        'мар': 3,
        'апр': 4,
        'мая': 5,
        'май': 5,
        'июн': 6,
        'июл': 7,
        'авг': 8,
        'сен': 9,
        'окт': 10,
        'ноя': 11,
        'дек': 12,}

get_date('15-тый четверг ноября')