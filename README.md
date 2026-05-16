# mplty: Typst extension for matplotlib

> [!NOTE]
> Experimental project!!

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