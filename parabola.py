import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x ** 2
plt.plot(x, y, label="y = x^2", color="black", linewidth=2)
plt.title("y=x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

x = np.linspace(-10, 10, 100)
y = x ** 2

