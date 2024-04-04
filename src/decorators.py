"""To run profiling without @profile decorator."""

import time
from functools import wraps

from loguru import logger
from line_profiler import LineProfiler


def profiler(f, *args):
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


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_taken = round(end - start, 5)
        logger.info(f"Time taken: {time_taken}")
        return result
    return wrapper

