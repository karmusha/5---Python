def filter_zero_coefficient(item):
    if item is None:
        return False
    
    (coefficient, _) = item

    if coefficient == 0:
        return False

    return True

def map_x(item: tuple[int, tuple[int, int]]):
    index, (coefficient, degree) = item

    element = ''
    if  degree == 0:
        element = element
    elif degree == 1:
        element = element + 'x'
    else:
        element = element + 'x^' + str(degree)

    return (index, coefficient, degree, element)

def map_coefficient(item: tuple[int, int, int, str]):
    (index, coefficient, degree, element) = item

    if coefficient == 1:
        element = element
    else:
        element = str(abs(coefficient)) + element
    
    return (index, coefficient, degree, element)

def map_sign(item: tuple[int, int, int, str]):
    (index, coefficient, degree, element) = item

    match (index, coefficient):
        case (0, coefficient) if coefficient > 0:
            element = element
        case (0, coefficient) if coefficient < 0:
            element = '-' + element
        case (index, coefficient) if index > 0 and coefficient > 0:
            element = '+ ' + element
        case (index, coefficient) if index > 0 and coefficient < 0:
            element = '- ' + element
    
    return (index, coefficient, degree, element)

def map_str(item: tuple[int, int, int, str]):
    (_, _, _, element) = item

    return element


def split_elements(line: str):
    res = ''
    for x in line:
        match x:
            case '+':
                yield res
                res = '+'
            case '-':
                yield res
                res = '-'
            case ' ':
                pass
            case '=':
                break
            case _:
                res = res + x
    yield res

def empty_filtration(item: str):
    if item == '':
        return False
    if item in ['\n', '\r']:
        return False
    
    return True

def element_to_tuple(item: str):
    x_match = False
    c_str = ''
    d_str = ''

    for x in item:
        if x_match == False and x == 'x':
            x_match = True
            d_str = x
            continue
        
        if x_match:
            d_str = d_str + x
        else:
            c_str = c_str + x
    
    return (c_str, d_str)

def parse_coefficient(item: str):
    coefficient: int
    match item:
        case '':
            coefficient = 1
        case x if x[0] == '+' or x[0] == '-':
            coefficient = x[1:]
            coefficient = int(coefficient) if coefficient != '' else 0
            if x[0] == '-':
                coefficient = -1 * coefficient
        case x:
            coefficient = int(x)

    return coefficient


DEGERE_MATCH_SYMBOLS = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'x': '',
    '^': '',
    '-': '-',
    '+': '',
    '\u00B2': '2',
    '\u00B3': '3',
    '\u00B9': '1',
    '\u2070': '0',
    '\u2074': '4',
    '\u2075': '5',
    '\u2076': '6',
    '\u2077': '7',
    '\u2078': '8',
    '\u2079': '9',
}

def parse_degree(item: str):
    match item:
        case '':
            default_degree = 0
        case x if x[0] == 'x':
            default_degree = 1
        case _:
            default_degree = 1
    
    degree = ''
    for x in item:
        match DEGERE_MATCH_SYMBOLS.get(x):
            case None:
                pass
            case x:
                degree += x

    if degree != '':
        degree = int(degree)
    else:
        degree = default_degree

    return degree

def parse_element(item: tuple[str, str]):
    (coefficient, degree) = item

    coefficient = parse_coefficient(coefficient)
    degree = parse_degree(degree)

    return (coefficient, degree)
