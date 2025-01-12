import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('auto-mpg.csv')
data['origin'].unique()
sns.countplot(x=data['cylinders'],hue=data['origin'])
plt.legend(title='Origin',loc='upper left',labels=['USA','Europe','Japan'])
plt.title('Count plot of cylinders')
plt.xlabel('No. of Cylinders')
plt.ylabel('No. of Cars')
plt.show()