from core.operations import (evaluate_discriminant, 
                             evaluate_degree, 
                             solve_two_real_solution, 
                             solve_one_real_solution, 
                             complex_solution, display_reduced_equation)


def solve_linear_equation(e : dict):
    """ bx + c = 0 """
    b = e.get(1)
    c = e.get(2)
    if b == 0:
        if c == 0:
            print ("Solution: Infinite solutions")
        else :
            print ("Solution: No solution")
    else :
        sol = -c / b
        print (f"Solution: x = {sol}")
    exit(0)



def solve_quadratic_equation(e : dict) :
    delta = evaluate_discriminant(e)
    if delta > 0:
        solve_two_real_solution(e, delta)
    elif delta == 0 :
        solve_one_real_solution(e, delta)
    else:
        complex_solution(e, delta)
    exit(0)
        

def execute(degree: int, e: dict) :
    print(f"Polynomial degree: {degree}")
    match degree:
        case 0:
            return e.get(0)
        case 1:
            return solve_linear_equation(e)
        case 2:
            return solve_quadratic_equation(e)
        case _:
            return None


def reduce_equation(left : dict, right: dict) :
    equation = left.copy()
    for k,v in right.items():
        if equation.get(k) : 
            equation[k] = equation[k] - v
        else :
            equation[k] = -1 * v 
    display_reduced_equation(equation)
    return equation


def equation_solver( left : dict, right: dict) :
    equation = reduce_equation(left, right)
    degree = evaluate_degree(equation)
    execute(degree, equation)
    