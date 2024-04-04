"""To run profiling without @profile decorator."""

import time
from functools import wraps
from typing import Callable

from line_profiler import LineProfiler
from loguru import logger


def profiler(f: Callable, *args):
    """Allows to pass functions to profile in command line.

    This removes the need to comment and uncomment @profile
    """
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "function",
    #     help="name of the functions where decorators will be used",
    #     type=str,
    #     nargs="+",  # allowing multiple arguments
    # )
    # argument = parser.parse_args()
    # logging.info(f"{argument.function}")

    lp = LineProfiler()
    f_wrapped = lp(f)
    f_wrapped(*args)
    lp.print_stats()


def timer(func: Callable) -> Callable:
    """Basic timer decorator to measure time taken for function call.

    Args:
        func (Callable): any function that takes positional/keyword arguments.

    Returns:
        Callable: wrapper function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function that wraps the target function to apply decorator."""
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_taken = round(end - start, 5)
        logger.info(f"Time taken: {time_taken}")
        return result

    return wrapper
