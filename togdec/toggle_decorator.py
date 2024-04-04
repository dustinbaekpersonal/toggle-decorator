"""Toggling decorator."""

import argparse
from typing import Callable


class ToggleDecorator:
    """Toggles decorator."""

    def __init__(self, decorator_func: Callable):
        """Initialize with decorator_func to toggle or not.

        _enabled attribute comes from argparse
        """
        self._enabled = self.parse_arg()
        self._decorator_func = decorator_func

    @staticmethod
    def parse_arg():
        """Parsing argument passed through command line."""
        parser = argparse.ArgumentParser()
        parser.add_argument("--enable", action="store_true")
        parser.add_argument("--disable", action="store_false")
        res = parser.parse_args()
        return res.enable

    @property
    def enabled(self):
        """Set enabled as getter method."""
        return self._enabled

    @enabled.setter
    def enabled(self, val: Callable = parse_arg):
        """Set enabled attribute as input val if boolean.

        Args:
            val (Callable): default parse_arg, which gives True or False
        """
        if not isinstance(val, bool):
            raise ValueError(f"{val} should be either True or False.")
        self._enabled = val

    def __call__(self, target_func: Callable):
        """Treats class instance as a function to call with parentheses.

        Args:
            target_func (Callable): pass target_func as argument to class instance

        Example:
            # decorator takes target_func as input
            @some_dec
            def some_func():
                return "asdf"

            This is same as:
            some_dec(some_func)

            So by treating class instance as callable function allows it to be decorator.
        """
        if self._enabled:
            return self._decorator_func(target_func)
        return target_func
