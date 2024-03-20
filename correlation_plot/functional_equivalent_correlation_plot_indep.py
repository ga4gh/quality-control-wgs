## correlation btn NPM and Dragen specific metric by reading the values in the input csv file coloumn header given to 'x' and 'y'
## draws a diagonal line which is independent of the scatter plot data and 
## which stays rooted to the axes even to resize the window
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
import scipy.stats as stats

df=pd.read_csv("1kg-100-samples-NPM-vs-Dragen.csv")
df.head()
x = df['yield_bp_q30_NPM']
y = df['yield_bp_q30_Dragen']
fig, ax = plt.subplots()
ax.scatter(x, y, c='tab:blue')
plt.xlabel('NPM')
plt.ylabel('Dragen')
plt.title('yield_bp_q30')
line = mlines.Line2D([0, 1], [0, 1], color='red')
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)
