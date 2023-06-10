# modified, from: https://github.com/Bumpkin-Pi/QuadraticRegression
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pow as toPower
import numpy as np
data = pd.DataFrame({
    "x": [100355, 200700, 272770, 330855, 388342],
    "y": [588.1, 2731.9, 5203.9, 7548.8, 11465.5],
    "y2": [647.6, 2812.2, 5406.6, 7931.3, 12018.3]
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
    plt.scatter([data.iloc[i].x], [data.iloc[i].y2], color="grey")

a = np.array([[Σx4, Σx3, Σx2], [Σx3, Σx2, Σx], [Σx2, Σx, n]])
b = np.array([Σx2y, Σxy, Σy])

solve = np.linalg.solve(a, b)

print((f'y = {solve[0]}x² + {solve[1]}x + {solve[2]}').replace("+ -", "- "))

x = np.linspace(100000, 400000, 1000)

y = (x**2)*solve[0] + solve[1]*x + solve[2]
plt.plot(x, y)

y2 = (x**2)*1.0283072801564901e-07 - x*0.011576809226273733 + 838.438394110624
plt.plot(x, y2)

font = {'family': 'monospace',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

plt.title('i7-11850H mpz_powm() benchmark; determines sqrt(-1) (mod p),\nlast random run / 1 deterministic (smallest quadratic non-residue) run', fontsize=12)
plt.ylabel('mpz_powm(res, a, p/4, p) runtime [s]', fontsize=12, fontdict=font)
plt.xlabel('prime p [decimal digits]  (C++ with libgmpxx; a=random/sqnr black/grey)', fontsize=12)

plt.show()
