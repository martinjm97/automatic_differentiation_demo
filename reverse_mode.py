""" A simple implementation of reverse-mode AD. """
import math


class Number:

    def __init__(self, value):
        self.value, self.grad_cache = value, None
        self.parents = []

    @property
    def grad(self):
        if self.grad_cache is None:
            self.grad_cache = sum(scale * parent.grad for scale, parent in self.parents)
        return self.grad_cache

    def __add__(self, other):
        n = Number(self.value + other.value)
        self.parents.append((1, n))
        other.parents.append((1, n))
        return n

    def __mul__(self, other):
        prod = Number(self.value * other.value)
        self.parents.append((other.value, prod))
        other.parents.append((self.value, prod))
        return prod

    def __repr__(self):
        return f'Number({self.value}, {self.grad})'


def sin(x):
    z = Number(math.sin(x.value))
    x.parents.append((math.cos(x.value), z))
    return z

# sin
x = Number(math.pi)
y = Number(2)
z = x * y + sin(x)
z.grad_cache = 1.0

print("The derivative with respect to x is:", x.grad)
print("The derivative with respect to y is:", y.grad)
