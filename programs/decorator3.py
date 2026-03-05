




def no_negative(fn):
    def wrapper(n):
        if n < 0:
            raise ValueError("Negative not allowed")
        return fn(n)
    return wrapper


@no_negative
def factorial(n):
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out

print(factorial(-3))


# factorial 5 = 5 * 4 * 3 * 2 * 1
# factorial 3 = 3 * 2 * 1