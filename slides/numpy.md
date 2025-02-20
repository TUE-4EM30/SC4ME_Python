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

In [2]: a.sum()
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
class: large-python-motion
---

## Application to the energy sources

Pandas use NumPy to allow for fast row and column operations

````md magic-move {at:1}
<<< @/snippets/numpy_index_v1.py python {1-3}
<<< @/snippets/numpy_index_v1_5.py python {4,5}
<<< @/snippets/numpy_index_v2.py python {4-11}
<<< @/snippets/numpy_index_v3.py python {4,5}
````

<div class="flex justify-center">
  <img src="/images/plot_v1.png" alt="v1" width="400" v-if="$slidev.nav.clicks === 0">
</div>

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/numpy_table_v1.py console 
<<< @/snippets/numpy_table_v2.py console 
<<< @/snippets/numpy_table_v3.py console 
<<< @/snippets/numpy_table_v3.py console 
````

---
layout: two-cols
class: large-python-motion
---

## Application to the energy sources

### $p = c(y-y_0)^a$

````md magic-move
<<< @/snippets/numpy_v0.py python 
<<< @/snippets/numpy_v1.py python {1}
<<< @/snippets/numpy_v2.py python {3}
````

<br>

````md magic-move
<<< @/snippets/numpy_v.py python 
<<< @/snippets/numpy_v4.py python 
<<< @/snippets/numpy_v5.py python {1-4,7}
<<< @/snippets/numpy_v6.py python {4-10}
````

::right::

&nbsp;

<div class="flex justify-center">
  <img src="/images/plot_log.png" alt="log" width="300" v-if="$slidev.nav.clicks === 0">
</div>

<div class="flex justify-center">
  <img src="/images/plot_log_1995.png" alt="log" width="300" v-if="$slidev.nav.clicks === 1">
</div>

<div class="flex justify-center">
  <img src="/images/plot_log_1995_noyear.png" alt="log" width="300" v-if="$slidev.nav.clicks >= 2">
</div>

<div class="flex justify-center">
  <img src="/images/plot_log_diff.png" alt="log_diff" width="300" v-if="$slidev.nav.clicks === 3">
</div>

<div class="flex justify-center">
  <img src="/images/plot_log_diff_filter.png" alt="log_diff" width="300" v-if="$slidev.nav.clicks === 4">
</div>

<div class="flex justify-center">
  <img src="/images/plot_log_1995_noyear_fit.png" alt="log_diff" width="300" v-if="$slidev.nav.clicks === 5">
</div>
---
layout: two-cols
---

## Optimization / vectorization

- Significant time profit for large lists

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

::right::

&nbsp;

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