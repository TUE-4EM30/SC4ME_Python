---
layout: two-cols
class: large-python-slide
---

## Intro to numpy
- A core library for efficient numerical computing in Python
- Optimized for handling large, multi-dimensional arrays and matrices
- Provides powerful tools for linear algebra, statistical operations, and mathematical computations

<br>

```python
import numpy

#Create two arrays
a = numpy.array([1,2,3,4])
b = numpy.array([1,3,5,7])
```
::right::

&nbsp;

``` python {lines:false}
In [1]: a.shape
Out [1]: (3,)

In [2]: a.sum
Out [2]: 10

In [3]: a+1
Out [3]: [2,3,4,5]

In [4]: a+b
Out [4]: [2,5,8,11]

In [5]: 2*a
Out [5]: [2,4,6,8]

In [6]: a*b
Out [6]: [1,6,15,28]

In [7]: numpy.outer(a,b)
Out [7]: #(4x4 matrix)
```


---
layout: two-cols
class: large-python-slide
---

## Relevant functions

Pandas use NumPy to allow for fast row and column operations

```python

Per_person = []
for country in df['Country']:
    Per_person.append(df.loc[country,'Total'] / df.loc[country,'Population'])

import numpy
Per_person = df['Total']/df['Population']

```

::right::

&nbsp;
<!-- alter table based on the commands -->

```console {lines:false}
       Country   Total   Population
0  Afghanistan    0.70    41128772
1      Albania    7.00     2842318
2      Algeria    0.68    44903228
3    Argentina   45.94    35588996
...
191    Vietnam  130.37    98186856
192      Yemen    0.60    33696612
193     Zambia   17.23    20017670
194   Zimbabwe    5.92    16320539

[195 rows x 2 columns]
```

---
layout: two-cols
---

## Application to the problem

- Significant time profit for large lists

::right::

&nbsp;

```py
# by hand
mean = (0+1+2+3+4+5+6+7+8+9)/10

# as list (0.000000 seconds)
lst = list(range(10))
mean = sum(lst) / len(lst)

# as numpy.array (0.000000 seconds)
array = numpy.arange(10)
mean = numpy.mean(array)

# as list (3.057409 seconds)
lst = list(range(100000000))
mean = sum(lst) / len(lst)

# as numpy.array (0.096082 seconds)
array = numpy.arange(100000000)
mean = numpy.mean(array)
```

---

## Optimization / vectorization

- From list to numpy array + explain vectorization (original lecture 7 slides)

```python
arr = np.array([1, 2, 3, 4, 5])
squared = []

for x in arr:
    squared.append(x ** 2)

squared = np.array(squared)
```

```python
squared = arr ** 2
```