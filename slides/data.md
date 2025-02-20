---
layout: two-cols
class: large-python-slide
---

## Pandas - Python Data Analysis Library

- Supports mixed data types (e.g., integers, floats, strings) within the same dataset
- Provides labeled indexing for both rows and columns for easier data manipulation
- Allows importing data from various file formats, including CSV, Excel, SQL, and JSON
- Offers built-in functions to retrieve dataset insights (.info(), .describe(), .head(), etc.)

<br>
```python
import pandas
```

::right::

&nbsp;

```python {lines:false}
In [1]: data = {'Student': ['John', 'Emily', 'Mike', 'Sarah'],
        'Age': [20, 22, 21, 23],
        'Score': [8.5, 9.2, 6.3, 7.4]}
        df = pandas.DataFrame(data)
Out [1]:    Student  Age  Score
        0     John   20    8.5
        1    Emily   22    9.2
        2     Mike   21    6.3
        3    Sarah   23    7.4

In [2]: df.shape
Out [2]: (4, 3)

In [3]: df = df.set_index('Student')
Out [3]:    Age  Score
    Student            
    John      20    8.5
    Emily     22    9.2
    Mike      21    6.3
    Sarah     23    7.4

In [4]: df.loc['John','Score']
Out [4]: 8.5
```

---
layout: two-cols
class: large-python-motion
---

## Application to the energy sources

````md magic-move {at:1}
<<< @/snippets/pandas_index_code.py python {1-4}
<<< @/snippets/pandas_index_code.py python {6-14}
<<< @/snippets/pandas_index_code.py python {16-18}
<<< @/snippets/pandas_index_code.py python {20-22}
````

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/pandas_index_v1.py console 
<<< @/snippets/pandas_index_v2.py console
<<< @/snippets/pandas_index_v3.py console
<<< @/snippets/pandas_index_v4.py console
````

- Reading in data files 
- Data manipulation (adding additional columns, removing columns, filtering data set, etc)