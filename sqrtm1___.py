# modified, from: https://github.com/Bumpkin-Pi/QuadraticRegression
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pow as toPower
import numpy as np
data = pd.DataFrame({
    "x": [100355, 200700, 272770, 330855, 388342],
    "y": [445.2, 2095.3, 3746.8, 5297.6, 8695.1]
})
data2 = pd.DataFrame({
    "x2": [100355, 200700, 272770, 330855, 388342, 1000000],
    "y2": [647.6, 2812.2, 5406.6, 7931.3, 12018.3, 93640.8]
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

for i in range(len(data2)):
    plt.scatter([data2.iloc[i].x2], [data2.iloc[i].y2], color="grey")

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

x = np.linspace(80000, 1020000, 1000)
x2 = np.linspace(80000, 1020000, 1000)

y = (x**2)*solve[0] + solve[1]*x + solve[2]
plt.plot(x, y)

y2 = (x**2)*1.0554194832720814e-07 - x*0.012866576114746796 + 963.5694282158807
plt.plot(x2, y2)

font = {'family': 'monospace',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

plt.title('i7-11850H mpz_powm() benchmark; determines sqrt(-1) (mod p),\nsmallest quadratic non-residue deterministic powm(); C++ with libgmpxx', fontsize=12)
plt.ylabel('mpz_powm(res, sqnr, p/4, p) runtime [s]', fontsize=8, fontdict=font)
plt.xlabel('prime p [decimal digits]  (bottom curve: faster 7600X CPU)            ', fontsize=12)

plt.show()
