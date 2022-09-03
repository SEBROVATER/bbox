from typing import Sequence

from bbox.sources.bbox_editor import BBoxEditor
from bbox.types import BBoxKind


class FloatBBox(BBoxEditor):
    def __init__(
        self,
        coords: Sequence,
        kind: BBoxKind = "x1y1x2y2",
        text: str = "",
        score: float = 0.5,
        **kwargs,
    ):
        super().__init__(coords, kind)
        self.text = text
        self.score = score
        self.__dict__.update(kwargs)

    def __repr__(self):
        bbox = f"FloatBBox(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2})"
        if text := self.text:
            text = f" - {self.text} ({self.score:.2f})"
        return f"<{bbox}{text}>"
