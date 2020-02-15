import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2.020 ** (-1 * x ** 3) - (x ** 3 * np.cos(x ** 4)) - 1.984


def plot_graph():
    t = np.arange(-1., 2., 0.001)
    fig, ax = plt.subplots()
    ax.plot(t, f(t))
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    plt.show()


# 1st Root: .85 ; Range: .05
def bisection_method(guess, delta):
    a = guess - delta
    b = guess + delta

    xn = 0
    poss_root_val = 10

    while abs(poss_root_val) > .0001:
        xn = (a + b)/2
        poss_root_val = f(xn)
        if abs(poss_root_val) < .0001:
            return xn
        if f(a)*f(xn) >= 0:
            a = xn
        elif f(b)*f(xn) >= 0:
            b = xn

    return xn


# 1st Root: -0.85 ; Range: .05
# 2nd Root: 1.26 ; Range: .02
# 3rd Root: 1.42 ; Range: .02
# 4th Root: 1.68 ; Range: .02
# 5th Root: 1.80 ; Range: .02
# 6th Root: 1.94 ; Range: .02
def main():

    print(bisection_method(-0.85, .05))
    print(bisection_method(1.26, .02))
    print(bisection_method(1.42, .02))
    print(bisection_method(1.68, .02))
    print(bisection_method(1.80, .02))
    print(bisection_method(1.94, .02))

    plot_graph()


main()
