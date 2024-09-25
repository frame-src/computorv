import re

def split_equation(line: str) -> list:
    splitted = line.split("=")
    if len(splitted) != 1 : 
        return None
    return splitted

def parse_polinom(polinom : str) : 
    terms = re.findall(r'([+-]?\d*\.?\d*)\s*\*\s*X\^(\d+)', polinom)
    term_dict = {}
    for term in terms:
        print(term)
    

def execute(line: str = "") :
    if not line :
        return None
    splitted_line = split_equation(line)
    if splitted_line == None :
        return None
    left = parse_polinom(splitted_line[0])
    right = parse_polinom(splitted_line[1])
    
    