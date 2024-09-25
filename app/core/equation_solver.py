import math


def evaluate_degree(e : dict) -> int :
    for k, v in reversed(list(e.items())) :
        if v != 0:
            return int(k)
    return 0


def solve_linear_equation(e : dict):
    pass


def solve_quadratic_equation(e : dict) :
    pass

def execute_solver(degree: int, e: dict) :
    match degree:
        case 0:
            return e['0']
        case 1:
            return solve_linear_equation(e)
        case 2:
            return solve_quadratic_equation(e)
        case _:
            return None



def equation_solver( left : dict, right: dict) :
    equation = left.copy()
    for k,v in right.items():
        if equation[k] : 
            equation[k] = equation[k] - v
        else :
            equation[k] = -1 * v 
    degree = evaluate_degree(equation)
    solution = execute_solver(degree, equation)
    