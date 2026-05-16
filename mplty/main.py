import typst
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from pathlib import Path
from tempfile import TemporaryDirectory
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def ax_typst(
    x,
    y,
    markup,
    ax=None,
    scale=1,
    page_rule="#set page(width: auto, height: auto, margin: 0pt)",
):
    if ax is None:
        ax = plt.gca()

    with TemporaryDirectory() as tmp:
        typst_file = Path(tmp) / "input.typ"
        output_file = Path(tmp) / "output.png"

        if page_rule:
            markup = f"{page_rule}\n{markup}"
        typst_file.write_text(markup, encoding="utf-8")

        typst.compile(str(typst_file), output=str(output_file), ppi=300)

        img = mpimg.imread(output_file)

    imagebox = OffsetImage(img, zoom=scale / 3)

    ab = AnnotationBbox(
        imagebox, (x, y), frameon=False, box_alignment=(0, 0), zorder=10
    )

    ax.add_artist(ab)
