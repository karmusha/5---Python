import model_import_data as mid
from view import view_console as vc
from view import view_html as vh
from view import view_xml as vx
from pathlib import Path

path = Path(__file__)
file = path.parent.joinpath('tel_book.txt')

command = input('Если хотите добавить данные в справочник, введите a: ')
if command == 'a':
    mid.add_to_txt()

command = input('Если хотите экспортировать данные из справочника, введите e: ')
if command == 'e':
    prompt = '''
Eсли хотите отобразить данные в консоли, введите c.
Если хотите экспортировать данные в html файл, введите h.
Если хотите экспортировать данные в xml файл, введите x.
Что выбрали: c, h или x? '''
    command = input(prompt)
    if command == 'c':
        vc.print_tel_book(file)
    if command == 'h':
        vh.export_to_html(file)
    if command == 'x':
        vx.export_to_xml(file)
