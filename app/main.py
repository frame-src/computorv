from core.utils.input_parser import execute as parse_input
from core.equation_solver import equation_solver as solve
def main():
    print("INSERT A POLINOM such as: '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0'")
    # to add the input part
    left, right = parse_input('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0') 
    if left :
        if right :
            solve( left, right)

if __name__ == "__main__":
    main()