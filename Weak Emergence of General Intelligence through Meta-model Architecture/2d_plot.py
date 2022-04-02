import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles


def f(x):
    return x**2


def g(x):
    return -x + 0.5


x_, y_ = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
ax = plt.axes()


x = np.arange(-1, 1, 0.1)
y = np.arange(-1, 1, 0.1)
plt.Circle((0, 0), np.sqrt(0.5))

ax.scatter(x_[:, 0], x_[:, 1], c=y_)
# ax.add_artist(plt.Circle((0, 0), np.sqrt(0.5), fill=False ))
# ax.plot(x, f(x))
# ax.plot(f(y), y)


ax.set_xlabel('x')
ax.set_ylabel('y')


plt.show()

