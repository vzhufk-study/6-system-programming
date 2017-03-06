# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 28.02.2017
import math

def u(x = 4):
    return math.tan(x)**2 + 1


class NumberDiff:
    def __init__(self, x, h):
        self.x = float(x)
        self.h = float(h)

    def set_h(self, value):
        self.h = float(value)

    def first(self, x):
        return (u(x + self.h) - u(x))/self.h

    def second(self, x):
        return (u(x) - u(x - self.h))/self.h

    def third(self, x):
        return (u(x + self.h) - u(x - self.h))/(2*self.h)

    def fourth(self, x):
        return (self.first(x) - self.second(x))/self.h

    def fifth(self, x):
        return (u(x + self.h) - 2*u(x) + u(x - self.h))/(self.h**2)

point = float(4)
for i in range(1, 6):
    print("10^-"+str(i))
    x = NumberDiff(point, 10**(-i))
    print(x.first(point))
    print(x.second(point))
    print(x.third(point))
    print(x.fourth(point))
    print(2 * (math.cos(point)**2) * math.tan(point))
