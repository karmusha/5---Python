from model_import_data import import_from_file
from pathlib import Path

file = Path(__file__)
file_html = file.parent.joinpath('export_tel_book.html')

def export_to_html(file):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head><h1>Фамилия имя отчество - телефон</h1></head>\n <body>\n'
    for f, i, o, t in import_from_file(file):
        html += '    <p {}>{} </p>\n'\
            .format(style, f'{f} {i} {o} - {t}')
    html += '  </body>\n</html>'
    
    with open(file_html, 'w') as page:
        page.write(html)

    return html