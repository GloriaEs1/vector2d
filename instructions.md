# Designing a Simple 2d Vector Class

## Instructions

- 2/14/23
    - Before changing **anything**, check out a new branch in which to work.

    - Write an `__init__` method for `Vector2d` that has positional parameters for the `x` and `y` components that correspond to the *instance variables* `self.x` and `self.y`

    - Write a `__repr__` method for the `Vector2d` class that returns a string such that `Vector2d(3, 4) == eval(repr(Vector2d(3, 4)))` is `True`

    - Write a `__str__` method for the `Vector2d` class such that `str(Vector2d(3, 4))` would return `'3i + 4j'`. (**i** and **j** are what many physicists and engineers use to denote the x and y directions)

    - Write an `__abs__` function that takes `self` as its only argument and returns the length of the hypotenuse of the right triangle with legs equal to `self.x` and `self.y`. For example, `abs(Vector2d(3, 4))` should return `5.0`.

    - Once you've finished today's work, commit your changes and push them to **your** repository.

    
