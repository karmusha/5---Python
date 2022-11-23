from model_import_data import import_from_file
from pathlib import Path

file = Path(__file__)
file_xml = file.parent.joinpath('export_tel_book.xml')

def export_to_xml(file):
    xml = '<xml>'
    for f, i, o, t in import_from_file(file):
        xml += '''
<Фамилия>{}</Фамилия>
<Имя>{}</Имя>
<Отчество>{}</Отчество>
<Телефон>{}</Телефон>
'''.format(f, i, o, t)
    xml += '</xml>'
    
    with open(file_xml, mode='w', encoding='utf-8') as page:
        page.write(xml)

    return xml
