---
layout: two-cols
---

## From C to Python

````md magic-move
<<< @/snippets/array_index.c c
<<< @/snippets/array_index_v1.py python {*|7}
<<< @/snippets/array_index_v2.py python {*|2}
<<< @/snippets/array_index_v3.py python
<<< @/snippets/array_index_v4.py python
````

::right::

<h1><br></h1>

- What does this `C` code do?
<v-click at="1">
    
- Literal translation to `Python`: a good idea?
</v-click>
<v-click at="2">
    
- Fibonacci numbers collected in a `list`
</v-click>
<v-click at="3">
    
- The `list` "knows" its size
</v-click>
<v-click at="4">
    
- The `list` can be iterated
</v-click>
<v-click at="5">
    
- The `list` "knows" the `index` function
</v-click>
<v-click at="6">

- Lots of modules available
- Easy installation of external modules:

```console {lines=false}
pip install fibonacci
```
</v-click>

---
layout: two-cols-header
---

## Object-Oriented programming

OOP is a programming paradigm based on *objects*, which are *abstract data structures* containing:
- Data (attributes or member variables)
- Procedures acting on the data (methods or member functions)

::left::

<<< @/snippets/array_index_v4.py python

::right::

- `fib8` is an object (instance) of type (class) `list`
- Data is stored internally in `fib8` (dynamic-array-like structure)
- `index(i)` is a method of `fib8`, which is equivalent to `list.index(fib8, i)` 

---
layout: iframe
url: https://docs.python.org/3/library/stdtypes.html
---

<!--Include page with built-in types-->

---
layout: center
class: red-background
hideInToc: true
---

# An example to explore built-in objects 

---
layout: image
image: images/f1champs.png
---

<!--Image with all F1 champions until 2024-->

---
layout: two-cols
---

##  F1 champions (version 1)

```py
# First champion in 1950
champions = ['Farina']

# The 1951 champion
champions.append("Fangio")

# The 1952-1953 champion
champions += ['Ascari']*2

# The 1954 champion
champions.insert(4, 'Hawthorn')

# Correction
champions.pop()
champions.append('Fangio')

years = range(1950,1950+len(champions))
for year, champion in zip(years,champions):
    print(f'{year}: {champion}')
```

::right::

## &nbsp;

- Use single or double quotes for string literals
- Adding items using `append`, `insert` or `+` operator
- Duplication items using the `*` operator
- Removing items using `pop`
- Iterating two lists at once using `zip`
- Pretty printing using format strings

---
layout: two-cols
---

## F1 champions (version 2)

```py
champions = [('Farina', 1950),
             ('Fangio', [1951,1954,1955,1956,1957]),
             ('Ascari', [1952,1953]),
             ('Hawthorn', 1958),
             ('Brabham', [1959,1960,1966])]

def list_champions(champions):
  for champion, years in champions:
    if isinstance(years, int):
      print(f'{years}: {champion}')
    elif isinstance(years, list):
      years = map(str, years)
      print(f'{", ".join(years)}: {champion}')

champions.sort()

list_champions(champions)

champions.sort(key=lambda item: min(item[1]))

list_champions(champions)
```

::right::

## &nbsp;

- `lists` and a `tuples` are both array data structures:
    - Items can have different types
    - A `list` is *mutable*, a `tuple` is not
    - A `list` is more flexible than a `tuple`
    - A `tuple` is more efficient than a `list`
- `tuples` and `lists` can be unpacked to promote readability
- `sort` can be customized by specifying a key function
- `map` applies a function to all items

---
layout: two-cols
---

## F1 champions (version 3)

```py
farina = {'First name' : 'Giuseppe',
          'Last name'  : 'Farina'  ,
          'Year(s)'    : 1950      ,
          'Nationality': 'Italy'}

fangio = {'First name' : 'Juan Manuel',
          'Last name'  : 'Fangio',
          'Year(s)'    : [1951,1954,1955,1956]}

fangio['Year(s)'].append(1957)

fangio.update({'Nationality': 'Argentina'})

champions = [farina, fangio]

for champion in champions:
  for key, value in champion.items():
    print(f'{key} : {value}')
```

::right::

## &nbsp;

- `dictionaries` store data in key-value pairs
- `dictionaries` are mutable
- a value can be accessed via its key
- `update` allows to add key-value pairs to a dictionary
- `items` iterates over the key-value pairs

---
layout: image-right
image: images/smalltalk.png
---

## Xerox PARC and Smalltalk

- **1970**: Printing company Xerox sets up a research center in Silicon Valley (Palo Alto Research Center)
- **1970s**: Development of Graphical User Interface (GUI) for Xerox Alto (1973)
- **1972**: Alan Kay and coworkers develop the first fully-formed *object oriented programming language*: SmallTalk
- **Today**: Independent technological development center