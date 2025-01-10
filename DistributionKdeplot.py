import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data= pd.read_csv('.vscode/auto-mpg.csv')
sns.kdeplot(data['cylinders'],shade=False) # shade=True will fill the area under the curve
# sns.distplot(data['cylinders'],bins=5,kde=True) is the same as sns.kdeplot(data['cylinders'],shade=False)
plt.title('Distribution of MPG')
plt.xlabel('No. of cylinders')
plt.show()
