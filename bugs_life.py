from math import sqrt


def shortest_distance(a, b, c):
    A = [sqrt(pow(a, 2) + pow((b + c), 2))]
    B = [sqrt(pow(b, 2) + pow((a + c), 2))]
    C = [sqrt(pow(c, 2) + pow((a + b), 2))]
    return min(list(A + B + C))


print(shortest_distance(1, 2, 3))
