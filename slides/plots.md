---
layout: two-cols
---

## Intro to MatplotLib


```python
import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

plt.title('Sine Wave')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Show the plot
plt.show()
```
::right::

&nbsp;

![Sinus Plot](/images/sinus_plot.png)

---

## Relevant functions

```python
plt.plot()	    #Line plot
plt.scatter()	#Scatter plot
plt.bar()	    #Bar chart
plt.hist()	    #Histogram
plt.pie()	    #Pie chart
plt.xlabel()	#X-axis label
plt.ylabel()	#Y-axis label
plt.title()	    #Title of plot
plt.legend()	#Add a legend
plt.grid()	    #Add grid lines
plt.show()	    #Display plot
plt.savefig()	#Save figure
```


---
layout: two-cols
---

## Application to example

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})

# Create scatter plot using Pyplot API
plt.scatter(df['x'], df['y'], color='blue', marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot (Pyplot Style)")
plt.show()
```

::right::

&nbsp;

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4))  # Create figure and axes
ax.scatter(df['x'], df['y'], color='red', marker='x')

# Customize labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Scatter Plot (Object-Oriented)")

plt.show()
```

---

## The MatplotLib Gallery

<iframe src="https://matplotlib.org/stable/gallery/index.html" width="100%" height="600px"></iframe>

---

## Taking it beyond Excel capabilities

-fancy plot