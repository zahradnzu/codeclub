def getSqrt(x: int) -> int:
    """ returns an x squared """
    return x*x

def getInt() -> int:
    """ returns an integer from stdin """
    return int(input("Vlozte integer:\n"))

n = getInt()
n_sqrt = getSqrt(n)
print(f"x je {n}, x squared je {n_sqrt}")

