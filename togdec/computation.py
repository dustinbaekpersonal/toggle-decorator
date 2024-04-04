"""Computation functions to put decorators."""

import random

from togdec.decorators import timer
from togdec.toggle_decorator import ToggleDecorator

toggle_timer = ToggleDecorator(timer)


@toggle_timer
def add_one(tmp: list[int]) -> list:
    """Adding one to list."""
    return [item + 1 for item in tmp]


def subtract_one(tmp: list[int]) -> list:
    """Subtracting one to list."""
    return [item - 1 for item in tmp]


def multiply_ten(tmp: list[int]) -> list:
    """Multiplying ten to list."""
    return [item * 10 for item in tmp]


def main():
    """Main function to call all."""
    num = 100_000
    tmp = [random.randint(-10, 10) for _ in range(num)]
    add_one_tmp = add_one(tmp)
    subtract_one_tmp = subtract_one(tmp)
    multiply_ten_tmp = multiply_ten(tmp)

    return add_one_tmp, subtract_one_tmp, multiply_ten_tmp


if __name__ == "__main__":
    num = 100_000
    tmp = [random.randint(-10, 10) for _ in range(num)]
    add_one_tmp = add_one(tmp)
    print(sum(add_one_tmp))
