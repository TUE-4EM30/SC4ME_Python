---
layout: two-cols
---

## Hello Numpy!
- Core library for efficient numerical computing
- Optimized for handling large, multi-dimensional arrays and matrices
- Powerful tools for linear algebra, statistical operations and mathematical computations

::right::

## &nbsp;

````md magic-move
```py {*}{lines:false}
In [1]: import numpy

In [2]: a = numpy.array([1,2,3,4])

In [3]: b = numpy.array([1,3,5,7])

In [4]: a.shape
Out[4]: (4,)

In [5]: a.sum()
Out[5]: 10

In [6]: a+1
Out[6]: [2,3,4,5]

In [7]: 2*a+3*b
Out[7]: array([ 5, 13, 21, 29])

In [8]: a*b
Out[8]: [1,6,15,28]

In [9]: numpy.dot(a,b)
Out[9]: 50
```
```py {*}{lines:false}
In [1]: import numpy

In [2]: a = numpy.array([1,2,3,4])

In [3]: b = numpy.array([1,3,5,7])

In [4]: c = a

In [5]: c[:] = [4,3,2,1]

In [6]: a
Out[6]: array([4, 3, 2, 1])

In [7]: c = b.copy()

In [8]: c[:] = [4,3,2,1]

In [9]: b
Out[9]: array([1, 3, 5, 7])
```
````

---
layout: two-cols
---

## Vectorization using Numpy

- Iterations in interpreted languages are slow
- Python excels in foreign function interfacing (FFI) 
- Under the hood, Numpy is implemented in `c`
- Write code such that expensive operations are performed in `c`
- Perform operations on an entire array (vectorization), instead of per element

::right::

## &nbsp;

```py
# By hand
mean = (0+1+2+3+4+5+6+7+8+9)/10

# As a list (0.000000 seconds)
lst = list(range(10))
mean = sum(lst) / len(lst)

# As a numpy.array (0.000000 seconds)
array = numpy.arange(10)
mean = numpy.mean(array)

# As a list (3.057409 seconds)
lst = list(range(100000000))
mean = sum(lst) / len(lst)

# As a numpy.array (0.096082 seconds)
array = numpy.arange(100000000)
mean = numpy.mean(array)
```

---
layout: two-cols
---

## Wind energy in NL

- Pandas is built on top of NumPy

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
---

## Wind energy in NL

Fitting $p = c(y-y_0)^a$

````md magic-move
<<< @/snippets/numpy_v0.py python 
<<< @/snippets/numpy_v1.py python {1}
<<< @/snippets/numpy_v2.py python {3}
<<< @/snippets/numpy_v3.py python 
<<< @/snippets/numpy_v4.py python {1-4,7}
<<< @/snippets/numpy_v5.py python {4-10}
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