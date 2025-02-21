---
style: apple-basic
css: styles.css
lineNumbers: true
hideInToc: true
class: red-background
---

#  Scientific Computing for Mechanical Engineering
##  Introduction to Object-Oriented Programming

---
src: ./slides/intro.md
---

<!-- slides imported from intro.md -->

---
src: ./slides/toc.md
---

<!-- table of contents -->

---
layout: center
class: red-background
---

# Introduction to Python

---
src: ./slides/python.md
---

<!-- slides imported from python.md -->

---
layout: center
class: red-background
---

# Object-Oriented Programming (OOP)

---
src: ./slides/oop.md
---

<!-- slides imported from oop.md -->

---
layout: center
class: red-background
---

# Data Analysis using Python

---
layout: two-cols
---

## Python libraries

<v-click>
- NumPy: Numerical computing with arrays.
</v-click>
<br>

<v-click>
- Pandas: Data manipulation and analysis.
</v-click>
<br>

<v-click>
- Matplotlib: 2D plotting and visualization.
</v-click>
<br>

<v-click>
- SciPy: Scientific and technical computing.
</v-click>
<br>

<v-click>
- Scikit-learn: Machine learning algorithms toolkit.
</v-click>
<br>

<v-click>
- TensorFlow: Deep learning framework by Google.
</v-click>
<br>

<v-click>
- Keras: High-level neural networks API.
</v-click>
<br>

<v-click>
- PyTorch: Deep learning library by Meta.
</v-click>
<br>

<v-click>
- Flask: Lightweight web application framework.
</v-click>

::right::

&nbsp;

<div class="flex justify-center">
  <img src="/images/Numpylogo.png" alt="numpy" width="300" v-if="$slidev.nav.clicks === 1">
</div>

<div class="flex justify-center">
  <img src="/images/Pandalogo.png" alt="pandas" width="300" v-if="$slidev.nav.clicks === 2">
</div>

<div class="flex justify-center">
  <img src="/images/Matplotliblogo.png" alt="matplotlib" width="300" v-if="$slidev.nav.clicks === 3">
</div>

<div class="flex justify-center">
  <img src="/images/scipylogo.jpg" alt="scipy" width="300" v-if="$slidev.nav.clicks === 4">
</div>

<div class="flex justify-center">
  <img src="/images/skikitlogo.png" alt="Scikit-learn" width="300" v-if="$slidev.nav.clicks === 5">
</div>

<div class="flex justify-center">
  <img src="/images/tensorflowlogo.png" alt="tensorflow" width="300" v-if="$slidev.nav.clicks === 6">
</div>

<div class="flex justify-center">
  <img src="/images/keraslogo.png" alt="keras" width="300" v-if="$slidev.nav.clicks === 7">
</div>

<div class="flex justify-center">
  <img src="/images/pytorchlogo.png" alt="pytorch" width="300" v-if="$slidev.nav.clicks === 8">
</div>

<div class="flex justify-center">
  <img src="/images/flasklogo.png" alt="flask" width="300" v-if="$slidev.nav.clicks === 9">
</div>

<!-- add snipped of the different libraries -->

---
layout: center
class: red-background
hideInToc: true
---

# An example to explore some modules 

---
layout: iframe
url: https://ourworldindata.org/explorers/energy?time=2023&hideControls=false&Total+or+Breakdown=Select+a+source&Energy+or+Electricity=Primary+energy&Metric=Per+capita+consumption&Select+a+source=Renewables&country=USA~GBR~CHN~OWID_WRL~IND~BRA~ZAF&tab=map
---

<!--Data set from "Our world in data"-->

---

## The annual growth of wind energy

### &nbsp;

### Visualize the annual wind energy production over the last 50 years and determine a trend line.

### &nbsp;

### Steps:
1. Reading and manipulating the data set using **Pandas**
  - What does the data set look like?
  - How can we alter the data set?
2. Plotting the relevant data using **Matplotlib**
  - How can we visualize the data set?
  - Can we identify a trend line?
3. Fitting a trend line using **Numpy**
  - How does the mathematical framework behind (a.o.) Pandas work?
  - How can we use arrays efficiently?

---
layout: center
class: red-background
---

# Pandas - Python Data Analysis Library

---
src: ./slides/data.md
---

<!-- slides imported from pandas.md -->

---
layout: center
class: red-background
---

# MatplotLib - Python Plotting Library

---
src: ./slides/plots.md
---

<!-- slides imported from plots.md -->

---
layout: center
class: red-background
---

# NumPy - Python Linear Algebra Library

---
src: ./slides/numpy.md
---

<!-- slides imported from numpy.md -->


---
layout: center
class: red-background
---

# Python & VSCode

---

<div class="flex justify-center">
  <img src="/images/VSCode.png" width="1200">
</div>

---

## Whats next?

- Self-study session
    - Continue to work on first assignment
    - Python and VSCode installation
    - Instruction set
- Next lecture
    - Creating objects
    - Introduction to Assignment II: Evolutionary algorithm
