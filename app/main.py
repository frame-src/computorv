from core.utils.input_parser import execute as parse_input
def main():
    print("INSERT A POLINOM such as: '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0'")
    parse_input() 

if __name__ == "__main__":
    main()