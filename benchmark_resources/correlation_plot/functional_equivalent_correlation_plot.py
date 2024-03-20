## ## correlation btn NPM and Dragen specific metric by reading the values in the input csv file coloumn header given to 'x' and 'y'

#pip3 install matplotlib numpy pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("1kg-100-samples-NPM-vs-Dragen.csv")
df.head()

x = df['yield_bp_q30_NPM']
y = df['yield_bp_q30_Dragen']
plt.scatter(x, y)
plt.xlabel('NPM')
plt.ylabel('Dragen')
plt.title('yield_bp_q30')
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
plt.savefig('yield_bp_q30.png')  
plt.show() 
plt.close()
