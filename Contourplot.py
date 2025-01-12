import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('auto-mpg.csv')
sns.displot(x=data['cylinders'], y=data['mpg'], kind='kde')
plt.title('Contour plot of cylinders and mpg')
plt.xlabel('No. of Cylinders')
plt.ylabel('Milage')
plt.show()
