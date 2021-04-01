import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=pd.DataFrame(np.random.rand(100,4),index=np.arange(100),columns=list("ABCD"))
# data=data.cumsum()
# print(data.head())
ax=data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class 2',ax=ax)
plt.show()