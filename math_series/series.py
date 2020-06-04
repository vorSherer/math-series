# fibonacci_cache = {}


def fibonacci(n):
    '''
    Given an integer value n, this function returns the nth value of the Fibonacci Numbers.
    '''
    if n < 0:
        prompt = "n must be an integer greater than or equal to 0."
        return prompt
    # elif n in fibonacci_cache:
    #     return fibonacci_cache(n)
    elif n == 0:
        value = 0
        return value
    elif n == 1 or n == 2:
        value = 1
        return value
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        # fibonacci_cache[n] = value
        return value


def lucas(n):
    pass


def sum_series(n, id1, id2):
    pass


if __name__ == "__main__":
    print(fibonacci(5))

