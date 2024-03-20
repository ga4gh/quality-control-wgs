## correlation btn NPM and Dragen specific metric by reading the values in the input csv file coloumn header given to 'x' and 'y'
## Adding the Lines
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import scipy.stats as stats

df=pd.read_csv("1kg-100-samples-NPM-vs-Dragen.csv")
df.head()
x = df['yield_bp_q30_NPM']
y = df['yield_bp_q30_Dragen']

x_min = df['yield_bp_q30_NPM'].min()
x_max = df['yield_bp_q30_NPM'].max()
y_min = df['yield_bp_q30_Dragen'].min()
y_max = df['yield_bp_q30_Dragen'].max()

lineStart = min(x_min,y_min)
lineEnd = max(y_max,y_max)

plt.scatter(x, y, c='tab:blue')
plt.xlabel('NPM')
plt.ylabel('Dragen')
plt.title('yield_bp_q30')
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})

plt.plot([lineStart, lineEnd], [lineStart, lineEnd], color = 'r', linestyle = 'dashed')
plt.xlim(lineStart, lineEnd)
plt.ylim(lineStart, lineEnd)
r, p = stats.pearsonr(x, y)
plt.annotate('r = {:.2f}'.format(r), xy=(0.1, 0.95), xycoords='axes fraction')
plt.savefig('yield_bp_q30_min-max.png')  
plt.show() 
plt.close()
