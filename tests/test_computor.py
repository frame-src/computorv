import pytest
import sys
import os

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
    # Test case: 5 * X^0 + 4 * X^1 = 4 * X^0
    left, right = parse_equation(equation)
    result = {k: v - right.get(k, 0) for k, v in left.items()}
    result = {k: round(v, 10) for k, v in result.items() if abs(v) > 1e-12}
    expected = {k: round(v, 10) for k, v in expected.items() if abs(v) > 1e-12}
    assert result == expected


def test_solve_degree_1(capsys):
    # Test case: 5 * X^0 + 4 * X^1 = 4 * X^0
    equation = "5 * X^0 + 4 * X^1 = 4 * X^0"
    left, right = parse_equation(equation)
    if left and right:
        solve(left, right)

    out = capsys.readouterr().out
    assert "Polynomial degree: 1" in out
    assert "-0.25" in out


def test_solve_degree_2(capsys):
    # Test case: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    left, right = parse_equation(equation)
    if left and right:
        solve(left, right)

    out = capsys.readouterr().out
    assert "Polynomial degree: 2" in out
    assert "Discriminant is strictly positive" in out


def test_solve_other(capsys):
    # Test case: 5 * X^0 + 4 * X^1 - 9.3 * X^2 + 9.4 * X^3 = 1 * X^0
    equation = "5 * X^0 + 4 * X^1 - 9.3 * X^2 + 9.4 * X^3 = 1 * X^0"
    left, right = parse_equation(equation)
    if left and right:
        solve(left, right)

    out = capsys.readouterr().out
    assert "The polynomial degree is strictly greater than 2, I can't solve." in out


def test_additional_cases(capsys):
    # Test case 1: 6.0 * X^1 + 3.0 * X^2 + 3.0 * X^0 = 0 * X^0
    equation1 = "6.0 * X^1 + 3.0 * X^2 + 3.0 * X^0 = 0 * X^0"
    left1, right1 = parse_equation(equation1)
    if left1 and right1:
        solve(left1, right1)
    out1 = capsys.readouterr().out
    assert "Polynomial degree: 2" in out1
    assert "Discriminant is negative" in out1 or "Discriminant is zero" in out1 or "Discriminant is strictly positive" in out1

    # Test case 2: 6 * X^1 + 3 * X^0 + 4 * X^2 = 4 * X^1
    equation2 = "6 * X^1 + 3 * X^0 + 4 * X^2 = 4 * X^1"
    left2, right2 = parse_equation(equation2)
    if left2 and right2:
        solve(left2, right2)
    out2 = capsys.readouterr().out
    assert "Polynomial degree: 2" in out2
    assert "Discriminant is negative" in out2 or "Discriminant is zero" in out2 or "Discriminant is strictly positive" in out2
    
    # Test case 3: X^3 - X^3 + X^2 + 12 * X^0 = 3 * X^1
    equation3 = "X^3 - X^3 + 1 * X^2 + 12 * X^0 = 3 * X^1"
    left3, right3 = parse_equation(equation3)
    if left3 and right3:
        solve(left3, right3)
    out3 = capsys.readouterr().out
    assert "Polynomial degree: 2" in out3
    if "Polynomial degree: 2" in out3:
        assert "Discriminant is negative" in out3 or "Discriminant is zero" in out3 or "Discriminant is strictly positive" in out3
    
    # Test case 4: 42*X^0 = 42*X^0
    equation4 = "42*X^0 = 42*X^0"
    left4, right4 = parse_equation(equation4)
    if left4 and right4:
        solve(left4, right4)
    out4 = capsys.readouterr().out
    assert "Polynomial degree: 0" in out4
    if "Polynomial degree: 0" in out4:
        assert "Every real number" in out4

    # Test case 5: 42*X^0 = 44*X^0
    equation5 = "42*X^0 = 44*X^0"
    left5, right5 = parse_equation(equation5)
    if left5 and right5:
        solve(left5, right5)
    out5 = capsys.readouterr().out
    assert "Polynomial degree: 0" in out5
    if "Polynomial degree: 0" in out5:
        assert "Impossible" in out5