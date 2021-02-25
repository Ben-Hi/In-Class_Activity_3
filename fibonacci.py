def fib_series(num):
    if num is 0:
        return 0

    elif num is 1:
        return 1

    else:
        return fib_series(num - 1) + fib_series(num - 2)

def factorial(num):
    if num == 0 or num == 1:
        return 1

    else:
        return num * factorial(num - 1)