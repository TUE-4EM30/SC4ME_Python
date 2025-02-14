---
layout: iframe
url: https://www.youtube.com/embed/ZTPrbAKmcdo
---

<!-- Youtube video on evolution of programming languages 1958-2025 -->

---

## Timeline

- **1989** Dutchy Guido van Rossum developed Python at CWI as a
descendant of ABC
- **1991** Release of the first version of Python (0.9.0)
- **1994** Release of Python 1.0
- **2000** Release of Python 2.0
- **2008** Release of Python 3.0
- **2024** Latest (stable) release: Python 3.13 

---

## Characteristics

- Main characteristics (original slide 12)

---

```py {*|2|16}
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

## PEP8

---
layout: two-cols
---

## Interpreter *vs* Script

### Interpreter (`python`/`ipython`)

```py {*}{lines:false}
In [1]: print( 'Hello world!' )
'Hello world!'

In [2]: a = 3

In [3]: a
Out[3]: 3

In [4]: b = 4

In [5]: ( a**2 + b**2 )**0.5
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
print( 'Hello world!' )

a = 3
b = 4

print( (a**2 + b**2)**0.5 )
```

```console {lines:false}
$ python pythagoras.py
'Hello world!'
5.0
```

- Execute script (through the command line)
- For executing a real program

</v-click>