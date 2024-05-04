import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import seaborn as sns

# plt.figure(figsize=(8,5))
# plt.style.use("seaborn-v0_8-dark")
# x = np.linspace(-5,5,20)
# plt.title("This is the title")
# plt.xlabel("x-axis", fontsize=14,)
# plt.ylabel("y-axis", fontsize=14)
# plt.plot(x, x**3, "o-", label="cubic")
# plt.plot(x, x**2, "r:", label="quadratic")
# plt.legend(loc=2)
# plt.xlim(-6.6, 6.6)
# plt.ylim(-10, 10)
# plt.grid()
# plt.show()

x = np.arange(11)
y = x**2

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Plot')
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title('Scatter')
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(2, 2, 3)
plt.bar(x, y)
plt.title('Bar')
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(2, 2, 4)
plt.loglog(x, y)
plt.title("Loglog")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()

plt.savefig('newfig.png')

plt.show()

# Comment to test
