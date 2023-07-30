# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path

def sort_files(source_folder, dirs_dictionary: dict):
    p = Path(source_folder)
    for i in p.iterdir():
        for k, v in dirs_dictionary.items():
            if i.suffix[1:] in v:
                save_path = Path(p/k)
                i.replace(save_path/i.name)
                break
            else:
                save_path = Path(p/'misc')

            if not Path.exists(save_path):
                Path.mkdir(save_path)
            


dirs = {
        'video': ['avi', 'mkv'],
        'text': ['txt', 'pdf', 'docx'],
        'image': ['jpeg', 'png'],
    }

source_folder = 'task4.files'

sort_files(source_folder, dirs)