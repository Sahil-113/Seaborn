import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df=pd.read_csv('.vscode/auto-mpg.csv')
sns.displot(df['cylinders'],kind='ecdf',color='red',linewidth=2) #ecdf is empirical cumulative distribution function
#sns.ecdfplot(df['cylinders'],color='red',linewidth=2) same as above
plt.xlabel('No. Cylinders')
plt.title('ECDF of No. Cylinders')  
plt.show()