import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import pandas as pd

np.random.seed(0)

#random seed 0, x 20, y 20, sigma 10 looks cool

l_x = 20
l_y = 20

df = np.zeros([l_y * l_x, 4])

for i in range(l_x):
    for j in range(l_y):
        df[i * l_y + j, 0] = i
        df[i * l_y + j, 1] = j
        df[i * l_y + j, 2] = np.random.standard_cauchy(size=None)
        df[i * l_y + j, 3] = np.random.normal(0, 5)

df = pd.DataFrame(data=df, columns=["x", "y", "z", "q"])

colors = "twilight"

plt.style.use('dark_background')
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['x'], df['y'], df['q'], cmap=colors, linewidth=0.2)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.tick_params(colors="black")
ax.spines['bottom'].set_color('red')
ax.set_ylabel(' ')
ax.set_xlabel(' ')
ax.set_zlabel(' ')
ax.grid(b = False)
plt.show()


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['x'], df['y'], df['z'], cmap=colors, linewidth=0.2)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.tick_params(colors="black")
ax.spines['bottom'].set_color('red')
ax.set_ylabel(' ')
ax.set_xlabel(' ')
ax.set_zlabel(' ')
ax.grid(b = False)
plt.show()