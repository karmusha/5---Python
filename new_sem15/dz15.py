# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import logging
from pathlib import Path
from collections import namedtuple
import argparse

FORMAT = '{msg}'

logging.basicConfig(filename='dz15.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    format=FORMAT,
                    style='{'
                    )

logger = logging.getLogger('__name__')

def get_path_from_user() -> Path:
    parser = argparse.ArgumentParser(description='path to directory for scan')
    parser.add_argument('path', metavar='P', type=str, help='please choose one folder for scan')
    args = parser.parse_args()
    path = args.path
    path = Path(path)
    if not path.is_dir():
        raise ValueError(f'"{path}" is not a directory')
    
    return path

Info = namedtuple('Info', ['name', 'ext', 'is_dir', 'parent'])

def item_to_tuple(path: Path):
    return Info(path.stem, path.suffix, path.is_dir(), str(path.parent.resolve()))

def get_tuples_from_path(path: Path):
    for item in path.iterdir():
        item = item_to_tuple(item)
        logger.info(f'{item.is_dir} {item.parent} {item.name} {item.ext}')
        yield item

if __name__ == '__main__':
    path = get_path_from_user()
    items = get_tuples_from_path(path)
    items = list(items)

