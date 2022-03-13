import datetime


def exclamation(string):
    return string + "!"

import functools
def emphasis(func):
    @functools.wraps(func) # optional
    def wrapper_do_twice(*args, **kwargs):
        value = func(*args, **kwargs) # this value is the original "hello!"
        return value + "!"         # let's add that "!"
    # this wrapper_do_twice is a function...
    # ...which takes a function and returns it's string return value, with an additional "!"
    return wrapper_do_twice

@emphasis
def exclamation_exclamation(*args, **kwargs):
    return exclamation(*args, **kwargs)

exclamation('hello')


def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        time_string = \
f"""Function Name:
{func.__name__}

Args:
{args, kwargs}

Start Time:
{start_time}

End Time:
{end_time}

Time Taken:
{(end_time-start_time).total_seconds()} seconds.
"""
        print(time_string)
        return result
    return wrapper
