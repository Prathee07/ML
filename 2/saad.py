#1
#Visualize the n-dimensional data using 3D surface plots.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

#3d surface plot
x = data['KM']
y = data['Doors']
z = data['Price']

ax = plt.axes(projection='3d')
ax.plot_trisurf(x,y,z,cmap="jet")
ax.set_title("3D Surface Plot")

plt.show()

#2 contour plots


#3
#Visualize the n-dimensional data using heat-map.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

#heat map
sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet',annot=True)
plt.show()

#4
# Visualize the n-dimensional data using Box-plot.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

#box plot
plt.title('Box Plot')
plt.boxplot([data["Price"],data["HP"],data["KM"]])

plt.xticks([1,2,3],["Price","HP","KM"])

plt.show()



