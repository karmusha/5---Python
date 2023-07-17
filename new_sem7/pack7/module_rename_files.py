from pathlib import Path

def search(extension: str) -> Path:
    gen = Path.cwd().glob(f'*.{extension}')
    for file in gen:
        yield Path(file)

def gen_new_name(original_name, new_name, position, new_extention):
    return f'{original_name}_{new_name}_{position}.{new_extention}'

def clean_extension(file_name: Path):
    return file_name.stem

def rename_files(new_name, search_extension, new_extention):
    for i, file in enumerate(search(search_extension), 1):
        file: Path = file
        file_without_extension = clean_extension(file)

        new_file = gen_new_name(file_without_extension, new_name, i, new_extention)
        print(f'{file} -> {new_file}')

        if file.exists():
            file.rename(new_file)


if __name__ == '__main__':
    rename_files('new', 'txt', 'png')
