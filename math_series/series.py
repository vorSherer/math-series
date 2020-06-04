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


def sum_series(n, id1, id2):
    pass


if __name__ == "__main__":
    print(fibonacci(2))
    # print(fibonacci(5))
    # print(fibonacci_cache)

