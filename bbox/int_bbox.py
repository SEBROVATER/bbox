from typing import Sequence

from bbox.bbox_editor import BBoxEditor
from bbox.bbox_img import BBoxImg
from bbox.types import BBoxKind


class IntBBox(BBoxEditor, BBoxImg):
    def __init__(self, coords: Sequence, kind: BBoxKind = "pascal_voc", text: str = "", score: float = 0.5, **kwargs):
        super().__init__(coords, kind, **kwargs)
        self.text = text
        self.score = score
        self.to_int()

    def __repr__(self):
        bbox = f"BBox(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2})"
        text = ""
        if self.text:
            text = f" - {self.text} ({self.score:.2f})"
        return f"<{bbox}{text}>"
