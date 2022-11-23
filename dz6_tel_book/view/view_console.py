def print_tel_book(file_path):
    with open (file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            line = line[:-1]
            print(line)