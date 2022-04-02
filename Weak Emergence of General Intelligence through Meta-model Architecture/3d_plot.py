import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles


def f(x, y):
    return x ** 2 + y ** 2 - 0.5

def g(x, y):
    return x + y - 0.5


x_, y_ = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
ax = plt.axes(projection='3d')


x = np.arange(-0.75, 0.75, 0.1)
y = np.arange(-0.75, 0.75, 0.1)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
Z2 = g(X, Y)

ax.plot_surface(X, Y, Z, alpha=0.5, color="black")
ax.plot_surface(X, Y, Z2, alpha=0.5, color="red")
ax.scatter(x_[:, 0], x_[:, 1], c=y_ , zdir='z', label='points in (x, z)')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

