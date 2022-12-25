from main import get_roots
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("Bdd.feature")


@given(parsers.parse("A coefficient is {A:d}"), target_fixture="coefficientA")
def input_A(A):
    return A


@given(parsers.parse("B coefficient is {B:d}"), target_fixture="coefficientB")
def input_B(B):
    return B


@given(parsers.parse("C coefficient is {C:d}"), target_fixture="coefficientC")
def input_C(C):
    return C


@when(parsers.parse("Solve the equation"), target_fixture="solvation")
def solving_the_equation(coefficientA, coefficientB, coefficientC):
    return get_roots(coefficientA, coefficientB, coefficientC)


@then(parsers.parse("Get number of roots {result:d} and compare"))
def getting_the_result(solvation, result):
    assert result == len(solvation)
