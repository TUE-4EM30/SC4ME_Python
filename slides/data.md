---
layout: two-cols
---

## Pandas

- Supports mixed data types (integers, floats, strings, *etc.*)
- Provides labeled indexing for both rows and columns
- Allows importing and exporting various file formats (CSV, Excel, SQL, JSON, *etc.*)
- Offers built-in functions to retrieve data set insights

::right::

&nbsp;

```python {lines:false}
In [1]: import pandas

In [2]: data = {'Student': ['John', 'Emily', 'Mike'],
        'Age': [20, 22, 21],
        'Score': [8.5, 9.2, 6.3]}
        df = pandas.DataFrame(data)
Out [2]:    Student  Age  Score
        0     John   20    8.5
        1    Emily   22    9.2
        2     Mike   21    6.3

In [3]: df.shape
Out [3]: (3, 3)

In [4]: df = df.set_index('Student')
Out [4]:    Age  Score
    Student            
    John      20    8.5
    Emily     22    9.2
    Mike      21    6.3

In [5]: df.loc['John','Score']
Out [5]: 8.5
```

---
layout: two-cols-header
---

## Renewable energy data set

::left::

````md magic-move {at:1}
<<< @/snippets/pandas_index_code.py python {1-4}
<<< @/snippets/pandas_index_code.py python {6-14}
<<< @/snippets/pandas_index_code.py python {16-18}
<<< @/snippets/pandas_index_code.py python {20-22}
````

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/pandas_index_v1.py console {*}{lines:false}
<<< @/snippets/pandas_index_v2.py console {*}{lines:false}
<<< @/snippets/pandas_index_v3.py console {*}{lines:false}
<<< @/snippets/pandas_index_v4.py console {*}{lines:false}
````