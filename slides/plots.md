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

<div class="flex justify-center">
    <img src="/images/sinus_plot.png" alt="sinus" width="400" >
</div>


---

## The MatplotLib Gallery

<iframe src="https://matplotlib.org/stable/gallery/index.html" width="100%" height="600px"></iframe>

---
layout: two-cols
---

## Different plotting methods

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
layout: two-cols
class: large-python-motion
---

## Application to the energy sources

````md magic-move {at:1}
<<< @/snippets/matplotlib_index_v1.py python {1-2}
<<< @/snippets/matplotlib_index_v1.py python {4-6}
<<< @/snippets/matplotlib_index_v2.py python {6-9}
<<< @/snippets/matplotlib_index_v3.py python {4-6,13-17}
````

```console {lines:false}
     Country      year   Wind  Solar  Nuclear  Hydro
0    Netherlands  1900    NaN    NaN      NaN    NaN
1    Netherlands  1901    NaN    NaN      NaN    NaN
2    Netherlands  1902    NaN    NaN      NaN    NaN
3    Netherlands  1903    NaN    NaN      NaN    NaN
4    Netherlands  1904    NaN    NaN      NaN    NaN
     ...
119  Netherlands  2019  11.51   5.40     3.91   0.07
120  Netherlands  2020  15.27   8.57     4.09   0.05
121  Netherlands  2021  18.00  11.30     3.83   0.09
122  Netherlands  2022  21.49  17.08     4.16   0.05
123  Netherlands  2023  28.97  21.15     4.00   0.06
    
[124 rows x 6 columns]
```


::right::

&nbsp;

<div class="flex justify-center">
  <img src="/images/plot_v1.png" alt="v1" width="500" v-if="$slidev.nav.clicks === 1">
</div>

<div class="flex justify-center">
  <img src="/images/plot_v2.png" alt="v2" width="500" v-if="$slidev.nav.clicks === 2">
</div>

<div class="flex justify-center">
  <img src="/images/plot_v3.png" alt="v3" width="500" v-if="$slidev.nav.clicks === 3">
</div>

---
layout: two-cols
---

## Application to the energy sources

- Can we find a relation in the yearly increase?

<v-click>

- In the logaritmic plot suggests so

</v-click>

::right::

&nbsp;

<div class="flex justify-center">
  <img src="/images/plot_v2.png" alt="v1" width="500" v-if="$slidev.nav.clicks === 0">
</div>

<div class="flex justify-center">
  <img src="/images/plot_log.png" alt="log" width="500" v-if="$slidev.nav.clicks === 1">
</div>