import re

def split_equation(line: str) -> list:
    splitted = line.split("=")
    if len(splitted) != 2 : 
        return None
    return splitted


def parse_polinom(polinom : str) -> dict : 
    """ Return something like:  { x0 : i_0, x1 : i_1, x2: i_3, ... , xn: i_n}"""
    
    terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*\*\s*X\^(\d+)', polinom)
    term_dict = {}
    for term in terms:
        value = float(term[0].replace(' ', ''))
        exp = int(term[1])
        term_dict[exp] = term_dict.get(exp, 0) + value
    return term_dict

    

def execute(line: str = "") -> tuple[list,list] :
    if not line :
        return None, None
    splitted_line = split_equation(line)
    if splitted_line == None :
        return None, None
    left = parse_polinom(splitted_line[0])
    right = parse_polinom(splitted_line[1])
    return left, right
    