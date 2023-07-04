# modified, from: https://github.com/Bumpkin-Pi/QuadraticRegression
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pow as toPower
import numpy as np
data = pd.DataFrame({
    "x": [110, 120, 129, 130, 140],
    "y": [9.79766, 11.74777, 13.48558, 13.66078, 15.28378]
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

x = np.linspace(100, 150, 1000)

y = (x**2)*solve[0] + solve[1]*x + solve[2]
plt.plot(x, y)

font = {'family': 'monospace',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }

plt.title('Six core 7600X CPU in 6C/12T mode cado-nfs.py benchmark;\nwith factor >10× of total cpu vs. elapsed time', fontsize=12)
plt.ylabel('log₂(factoring runtime) [s]', fontsize=12, fontdict=font)
plt.xlabel('RSA-x [x decimal digits]', fontsize=12)

plt.show()
