
## Python: a fourth generation language

- A short history (original slide 14)
- Main characteristics (original slide 12)
- Most popular programming language to date (original slide 14)

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

<h1><br></h1>

<v-click>

### Script (`pythagoras.py`)
 
```py
print( 'Hello world!' )

a = 3
b = 4

print( (a**2 + b**2)**0.5 )
```

```console {*}{lines:false}
$ python pythagoras.py
'Hello world!'
5.0
```

- Execute script (through the command line)
- For executing a real program

</v-click>