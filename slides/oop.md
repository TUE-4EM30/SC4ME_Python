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

## Object-Oriented programming

Original slide 22

---

##  Shopping list (version 1)

```py
shopping_list = ['flour (2 cups)', 'sugar (1 cup)']
shopping_list.append('brown sugar (1 cup)')
shopping_list.append('baking soda (1 tsp)')
shopping_list.append('salt (1/2 tsp)')
shopping_list.append('butter (1 cup)')
shopping_list.append('vanilla extract (1 tsp)')
shopping_list.append('eggs (2)')
shopping_list.append('chocolate chips (2 cups)')
shopping_list.append('walnuts (optional, 1 cup)')
```

Animated code with typical list operations:
- strings: explain single and double quote usage
- append
- insert
- sort
- reverse
- pop
- print

---

## Shopping list (version 2)

```py
shopping_list.append(('flour (cup)', 2))
shopping_list.append(('sugar (cup)', 1))
shopping_list.append(('brown sugar (cup)', 1))
shopping_list.append(('baking soda (tsp)', 1))
shopping_list.append(('salt (1/2 tsp)', 1))
shopping_list.append(('butter (1 cup)', 1))
shopping_list.append(('vanilla extract (1 tsp)', 1))
shopping_list.append(('eggs', 2))
shopping_list.append(('chocolate chips (cup)', 2))

for item, amount in shopping_list:
    print(f'{item} : {amount}')

```

- Adding the number of items using a tuple (milk, 3)
- Explain difference between tuple and list
- Loop over the list and demonstrate tuple unpacking
- Format string

---

## Shopping list (version 3)

```py
shopping_list = []

flour = {'name':'flour', 'unit':'cup', 'prize/unit':1.25}
shopping_list.append((flour,2))

```

- Explain dictionary 

---

## Shopping list (version 4)

- Prize calculation
- First with loop, then with comprehensions (Original slide 30)

---

## Intermezzo: Xerox PARC and Smalltalk

- Original slide 38