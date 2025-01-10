import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
data= pd.read_csv('.vscode/auto-mpg.csv')
sns.distplot(data['cylinders'],bins=5,kde=True)
plt.title('Distribution of MPG')
plt.xlabel('No. of cylinders')
plt.show()
