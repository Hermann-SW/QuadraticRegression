# modified, from: https://github.com/Bumpkin-Pi/QuadraticRegression
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pow as toPower
import numpy as np
data = pd.DataFrame({
    "x": [10000, 36481, 100355, 200700, 272770, 330855, 388342],
    "y": [0.7, 12.9, 139.5, 648.1, 1262.5, 1878.6, 2524.1]
})

Σx = 0
Σy = 0
Σxy = 0
Σx2 = 0
Σx3 = 0
Σx4 = 0
Σx2y = 0
n = len(data)

a = 0
b = 0
c = 0

for i in range(len(data)):
    Σx += data.iloc[i].x
    Σy += data.iloc[i].y
    Σxy += data.iloc[i].x * data.iloc[i].y
    Σx2 += toPower(data.iloc[i].x, 2)
    Σx3 += toPower(data.iloc[i].x, 3)
    Σx4 += toPower(data.iloc[i].x, 4)
    Σx2y += toPower(data.iloc[i].x, 2) * data.iloc[i].y

    plt.scatter([data.iloc[i].x], [data.iloc[i].y], color="black")

a = np.array([[Σx4, Σx3, Σx2], [Σx3, Σx2, Σx], [Σx2, Σx, n]])
b = np.array([Σx2y, Σxy, Σy])

solve = np.linalg.solve(a, b)

print((f'y = {solve[0]}x² + {solve[1]}x + {solve[2]}').replace("+ -", "- "))

x = np.linspace(0, 400000, 1000)

y = (x**2)*solve[0] + solve[1]*x + solve[2]
plt.plot(x, y)

font = {'family': 'monospace',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

plt.title('Python sympy gaussian integer gcd() benchmark; with\nprecomputed sqrtm1 = sqrt(-1) (mod p) — no speedup using gmpy2', fontsize=12)
plt.ylabel('gcd(p, sqrtm1 + I) runtime [s] (on i7-11850H)', fontsize=12, fontdict=font)
plt.xlabel('prime p [decimal digits]', fontsize=12)

plt.show()
