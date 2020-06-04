from functools import lru_cache


@lru_cache(maxsize = 1000)
def fibonacci(n):
    '''
    Given an integer value n, this function returns the nth value of the Fibonacci Numbers.
    '''
    if isinstance(n, str):
        raise TypeError("n must be an integer greater than or equal to 0.")
    elif n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    elif n == 0:
        value = 0
        return value
    elif n == 1 or n == 2:
        value = 1
        return value
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        return value


def lucas(n):
    '''
    Given an integer value n, this function returns the nth value of the Lucas Numbers.
    '''
    if n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    elif n == 0:
        value = 2
        return value
    elif n == 1:
        value = 1
        return value
    elif n >= 2:
        value = lucas(n-1) + lucas(n-2)
        return value


def sum_series(n, id1=0, id2=1):
    # pass
    '''
    Given an integer value n and two optional terms id1 and id2, this function returns the nth value of the user-specified Fibonacci or Lucas numbers (defaults to Fibonacci if no optional terms provided).
    '''
    if n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    elif id1 == 0 and id2 == 1:
        value = fibonacci(n)
        return value
    elif id1 == 2 and id2 == 1:
        value = lucas(n)
        return value
    else:
        warning = "Sorry, that combination has not yet been defined."
        return warning


if __name__ == "__main__":
    print("fib(2) = ", fibonacci(2))
    print("fib(5) = ", fibonacci(5))
    print("luc(10) = ", lucas(10))
    print("Sum_ser(0, 0, 1) = ", sum_series(0, 0, 1))
    print("Sum_ser(0, 2, 1) = ", sum_series(0, 2, 1))
    print("Sum_series defaults to fib: ", sum_series(5))
    print("fib(200) = ", fibonacci(200))
    

