##def manhattan(a, b):
  ##  return sum(abs(x - y) for x, y in zip(a, b))

"""def manhattan(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]
    return abs(d_x) + abs(d_y)

def euclidean(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]
    return (d_x**2 + d_y**2)**0.5"""

# Minkowski mesafesi: p=1 için Manhattan, p=2 için Euclidean özel hallerini verir.

def minkowski(a, b, p=2):
    return sum(abs(x - y) ** p for x, y in zip(a, b)) ** (1 / p)

def manhattan(a, b):
    return minkowski(a, b, p=1)

def euclidean(a, b):
    return minkowski(a, b, p=2)