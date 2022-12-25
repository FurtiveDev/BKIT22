Feature: Scenario Outline
  Testing the code

  Scenario Outline: Solve the equation
    Given A coefficient is <A>
    And B coefficient is <B>
    And C coefficient is <C>
    When Solve the equation
    Then Get number of roots <D> and compare

    Examples:
      | A  | B  | C  | D |

      | 1  | -1 | 1  | 0 |
      | 1  | 0  | 0  | 1 |
      | 1  | -2 | -8 | 2 |
      | 10 | -5 | 0  | 3 |
      | 4  | -5 | 1  | 4 |