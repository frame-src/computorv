import math

def evaluate_discriminant(e) :
    """ b^2 - 4ac"""
    print(e)
    a = e.get(2)
    b = e.get(1)
    c = e.get(0)
    delta = (b * b) - (4 * a * c)
    return delta


def evaluate_degree(e : dict) -> int :
    for k, v in reversed(list(e.items())) :
        if v != 0:
            return int(k)
    return 0

def display_reduced_equation(e : dict):
    eq = ""
    for k, v in reversed(list(e.items())) :
        if v != 0:
            if v > 0: 
                eq += f"{v} * X^{k} + "
            else:
                eq = eq[:-2]
                eq += f"- {-v} * X^{k} + "
        else:
            pass
    print(f"Reduced equation: {eq[:-2]}= 0")


def solve_two_real_solution(e: dict, delta: float) :
    print(f"Discriminant is strictly positive, the two solutions are:")
    print(e)
    a = e.get(2)
    b = e.get(1)
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print(root1)
    print(root2)


def solve_one_real_solution(e: dict, delta:float) :
    print(f"Discriminant is zero. One real solution:")
    a = e.get(2)
    b = e.get(1)
    root = -b / (2 * a)
    print(root)


def complex_solution(e: dict, delta:float) :
    print(f"Discriminant is negative. Two complex solutions:")
    a = e.get(2)
    b = e.get(1)
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-delta) / (2 * a)
    print(f"X1 = {real_part} + {imaginary_part}i")
    print(f"X2 = {real_part} - {imaginary_part}i")