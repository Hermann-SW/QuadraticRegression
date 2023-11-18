# modified, from: https://github.com/Bumpkin-Pi/QuadraticRegression
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pow as toPower
import numpy as np
data = pd.DataFrame({
    "x": [110503, 132049, 216091, 756839, 859433, 1257787],
    "y": [   207,    319,    864,  13898,  18810,   43917],
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

x = np.linspace(100000, 1300000, 1000)

y = (x**2)*solve[0] + solve[1]*x + solve[2]
plt.plot(x, y)

#y2 = (x**2)*9.925562577486448e-08 - x*0.008591031541973985 + 522.9552053486736
#plt.plot(x, y2)

font = {'family': 'monospace',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

plt.title('AMD 7600X foursquares() benchmark;\ndetermines sum of 4 squares for M_p', fontsize=12)
plt.ylabel('foursquares(M_p) runtime [s]', fontsize=12, fontdict=font)
plt.xlabel('prime p of Mersenne prime M_p=2^p-1', fontsize=12)

plt.show()
