---
layout: default
---

## Introduction of the problem to be considered

<div style="width: 100%; display: flex; justify-content: center;">
    <div style="transform: scale(0.7); transform-origin: top left; width: 125%; height: 750px; overflow: hidden;">
        <iframe src="https://ourworldindata.org/explorers/energy?time=2023&hideControls=false&Total+or+Breakdown=Select+a+source&Energy+or+Electricity=Primary+energy&Metric=Per+capita+consumption&Select+a+source=Renewables&country=USA~GBR~CHN~OWID_WRL~IND~BRA~ZAF&tab=map" loading="lazy" style="width: 100%; height: 600px; border: 0px none;" allow="web-share; clipboard-write"></iframe>
    </div>
</div>
---

## Popular Python libraries

- NumPy: Numerical computing with arrays.
- Pandas: Data manipulation and analysis.
- Matplotlib: 2D plotting and visualization.
- SciPy: Scientific and technical computing.
- Scikit-learn: Machine learning algorithms toolkit.
- TensorFlow: Deep learning framework by Google.
- Keras: High-level neural networks API.
- PyTorch: Deep learning library by Meta.
- Flask: Lightweight web application framework.
- Django: High-level web framework.

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
class: large-python-slide
---
## Relevant functionality

Full data set is significantly larger so cannot be done by hand anymore

```python
import panda
# Read in the data from a csv. file (or other document types)
df = pandas.read_csv('data_renewables.csv') # renewable energy consumption (TWh)
df

# add a row with the global reneable energy consumption
global_row = pd.DataFrame({
    "Country": ["World"],
    "Hydro": [df["Hydro"].sum()],
    "Nuclear": [df["Nuclear"].sum()],
    "Solar": [df["Solar"].sum()],
    "Wind": [df["Wind"].sum()]
})
df = pd.concat([df, global_row], ignore_index=True)

# Add a row of total renewable energy consumption
df["Total"] = df[["Hydro", "Nuclear", "Solar", "Wind"]].sum(axis=1)

# Reindex for wind energy consumption
df = df.sort_values(by="Wind", ascending=False).reset_index(drop=True)
```

::right::

&nbsp;
<!-- alter table based on the commands -->

```console {lines:false}
       Country   Hydro  Nuclear  Solar  Wind
0  Afghanistan    0.62      0    0.08   0.00
1      Albania    6.96      0    0.04   0.00
2      Algeria    0.01      0    0.66   0.01
3    Argentina   23.89   4.95    2.94  14.16
...
191    Vietnam   95.96      0   26.37   8.04
192      Yemen    0.00      0    0.60   0.00
193     Zambia   17.09      0    0.14   0.00
194   Zimbabwe    5.88      0    0.03   0.00

[195 rows x 4 columns]
```
- Reading in data files
- Data manipulation (adding additional columns, removing columns, filtering data set, etc)


---
## Application to the energy sources

- Code with explanation
- Ends with next step for problem