import pytest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from core.utils.input_parser import execute as parse_equation
from core.equation_solver import equation_solver as solve


@pytest.mark.parametrize(
    "equation, expected",
    [
        ("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0", {0: 4.0, 1: 4.0, 2: -9.3}),
        ("5 * X^0 + 4 * X^1 = 4 * X^0", {0: 1.0, 1: 4.0}),
        ("42 * X^0 = 42 * X^0", {}),
    ],
)
def test_parse_equation(equation, expected):
    left, right = parse_equation(equation)  # <- NB it returns a tuple
    result = {k: v - right.get(k, 0) for k, v in left.items()}
    result = {k: round(v, 10) for k, v in result.items() if abs(v) > 1e-12}
    expected = {k: round(v, 10) for k, v in expected.items() if abs(v) > 1e-12}
    assert result == expected


def test_solve_degree_1(capsys):
    equation = "5 * X^0 + 4 * X^1 = 4 * X^0"
    left, right = parse_equation(equation)  # parse left/right separately
    if left and right:
        solve(left, right)  # pass both to solve

    out = capsys.readouterr().out
    assert "Polynomial degree: 1" in out
    assert "-0.25" in out


def test_solve_degree_2(capsys):
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    left, right = parse_equation(equation)
    if left and right:
        solve(left, right)

    out = capsys.readouterr().out
    assert "Polynomial degree: 2" in out
    assert "Discriminant is strictly positive" in out


def test_solve_other(capsys):
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 + 9.4 * X^3 = 1 * X^0"
    left, right = parse_equation(equation)
    if left and right:
        solve(left, right)

    out = capsys.readouterr().out
    assert "The polynomial degree is strictly greater than 2, I can't solve." in out
