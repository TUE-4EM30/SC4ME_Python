---
layout: iframe
url: https://www.youtube.com/embed/ZTPrbAKmcdo
---

<!-- Youtube video on evolution of programming languages 1958-2025 -->

---
layout: two-cols-header
---

## Python's timeline

::left::

- **1989** Dutchy Guido van Rossum developed Python at CWI as a
descendant of ABC
- **1991** Release of the first version of Python (0.9.0)
- **1994** Release of Python 1.0
- **2000** Release of Python 2.0
- **2008** Release of Python 3.0
- **2024** Latest release: Python 3.13 

::right::

<div class="flex justify-center">
  <img src="/images/vanrossum.jpg" width="300">
</div>

---
layout: two-cols-header
---

## A fourth generation language (4GLs)

::left::

- High-level abstraction
- Ease of use and readability
- Rapid development: 
    - Built-in functionality
    - No compilation
    - Platform independent
- Extensive libraries and frameworks

::right::

<div class="flex justify-center">
  <img src="/images/python.svg" width="600">
</div>

---
layout: two-cols
---

## Interpreter *vs* Script

### Interpreter (`python`/`ipython`)

```py {*}{lines:false}
In [1]: print('Hello world!')
'Hello world!'

In [2]: a = 3

In [3]: a
Out[3]: 3

In [4]: b = 4

In [5]: (a**2 + b**2)**0.5
Out[5]: 5.0
```

- Read-Eval-Print-Loop (like Matlab console)
- For testing code snippets
- Watch out with memory!

::right::

## &nbsp;

<v-click>

### Script (`pythagoras.py`)
 
```py
print('Hello world!')

a = 3
b = 4

print((a**2 + b**2)**0.5)
```

```console {lines:false}
$ python3 pythagoras.py
'Hello world!'
5.0
```

- Execute script (through the command line)
- For executing a real program

</v-click>

---

```python {*|1,2|10,16}
In [1]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---
layout: two-cols
---

## Stimulating readability

````md magic-move
```py
import math

a_list = [1,2,3]
b_list = [4,5,6]

for i in range(3):
  for j in range(3):
    a = a_list[i]
    b = b_list[j]
    c = math.sqrt(a**2+b**2)
   print(f'{a}²+{b}²={c:4.3f}²')
```
```py
import math

a_list = [1,2,3]
b_list = [4,5,6]

for i in range(3):
  for j in range(3):
    a = a_list[i]
    b = b_list[j]
    c = math.sqrt(a**2+b**2)
    print(f'{a}²+{b}²={c:4.3f}²')
```
```py
import math

a_list = [1,2,3]
b_list = [4,5,6]

for a in a_list:
  for b in b_list:
    c = math.sqrt(a**2+b**2)
    print(f'{a}²+{b}²={c:4.3f}²')
```
```py
import math

a_list = [1, 2, 3]
b_list = [4, 5, 6]

for a in a_list:
  for b in b_list:
    c = math.sqrt(a**2 + b**2)
    print(f'{a}² + {b}² = {c:4.3f}²')
```
````

::right::

## &nbsp;

- White space matters!

```console {lines=false}
  File "<stdin>", line 11
    print(f'{a}²+{b}²={c:4.3f}²')
                                 ^
IndentationError: unindent does not 
match any outer indentation level
```

<v-click at=1>

- Consistent indentation enforced

</v-click>

<v-click at=2>

- Iterate values, not indices

</v-click>

<v-click at=3>

- Style recommendations (PEP8):
    - Add spaces after each comma in list
    - Add spaces around operators
    - ...

</v-click>

---
layout: iframe
url: https://peps.python.org/pep-0008
---

<!-- PEP8 website -->