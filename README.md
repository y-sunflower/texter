# mplty: Typst extension for matplotlib

> [!NOTE]
> Experimental project!

`mplty` bridges [Typst](https://typst.app/), a modern typesetting system, and [matplotlib](https://matplotlib.org/), Python's standard plotting library. It lets you render rich Typst markup (styled text, boxes, math equations and pretty much **all what Typst can do**) and place the result directly onto a matplotlib Axes at any data coordinate.

Matplotlib's built-in text rendering is powerful but limited when it comes to inline customization. `mplty` solves this by handing all typesetting work to Typst, which compiles your markup to a high-resolution image that is then embedded in the figure, giving you publication-quality annotations without leaving Python.

<br>

## Quick start

```py
from mplty import ax_typst

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])

typst_markup = r"""
#box(
  stroke: yellow,
  inset: 4pt,
  text(font: "Roboto", fill: red)[*hello* world in _italic_]
)
"""
ax_typst(1.5, 2, typst_markup)
```

![](./quick-start.png)

<br>


## Installation

```
pip install git+https://github.com/y-sunflower/mplty.git
```

