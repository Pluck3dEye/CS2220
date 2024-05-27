# Dung K.V. Nguyen (1607859)

import numpy as np
import matplotlib.pyplot as plt


# Problem #9 page 217
def my_poly_plotter(n, x):
    plt.figure(figsize=(14, 10))
    plt.style.use("seaborn-v0_8-dark")
    plt.title(f"Polynomials up to degree {n}")
    plt.xlabel("x-axis", fontsize=14)
    plt.ylabel("y-axis", fontsize=14)
    for i in range(1, n + 1):
        plt.plot(x, x ** i, label=f"Degree {i}")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


my_poly_plotter(10, np.linspace(-1, 1, 200))
