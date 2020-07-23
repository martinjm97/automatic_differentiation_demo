""" A simple implementation of forward-mode AD. """
import math


class Number:

    def __init__(self, value, grad=None):
        self.value, self.grad = value, grad

    def __add__(self, other) -> 'Number':
        return Number(self.value + other.value, self.grad + other.grad)

    def __mul__(self, other) -> 'Number':
        return Number(self.value * other.value, self.value * other.grad + self.grad * other.value)

    def __repr__(self) -> str:
        return f'Number({self.value}, {self.grad})'


class sin(Number):
    def __init__(self, arg: Number):
        self.value, self.grad = math.sin(arg.value), math.cos(arg.value) * arg.grad


x = Number(math.pi, 1)
y = Number(2, 0)
print('The derivative with respect to x is:', (x * y + sin(x)).grad)

# Compute the derivative with respect to y
x = Number(math.pi, 0)
y = Number(2, 1)
print('The derivative with respect to y is:', (x * y + sin(x)).grad)