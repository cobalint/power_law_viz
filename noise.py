import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
import pandas as pd

np.random.seed(0)
n = 100
df = np.zeros([n, 3])

for i in range(n):
    df[i, 0] = i
    df[i, 1] = np.random.normal(0, 10)
    df[i, 2] = np.random.standard_cauchy()

df = pd.DataFrame(df, columns=["x", "y", "z"])

plt.style.use('dark_background')
plt.plot(df["x"], df["y"], "white")
# plt.fill_between(df["x"], df["y"], color = "white")
plt.tick_params(colors="black")
plt.show()

plt.plot(df["x"], df["z"], "white")
# plt.fill_between(df["x"], df["z"], color="white")
plt.tick_params(colors="black")
plt.show()