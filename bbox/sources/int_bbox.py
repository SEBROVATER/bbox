from typing import Sequence

from .bbox_editor import BBoxEditor
from .bbox_img import BBoxImg
from ..types import BBoxKind


class IntBBox(BBoxEditor, BBoxImg):
    def __init__(
        self,
        coords: Sequence,
        kind: BBoxKind = "x1y1x2y2",
        text: str = "",
        score: float = 0.5,
        **kwargs,
    ):
        super().__init__(coords, kind)
        self.round_coords()
        self.text = text
        self.score = score

        self.__dict__.update(kwargs)

    def round_coords(self) -> None:
        self.x1 = round(self.x1)
        self.y1 = round(self.y1)
        self.x2 = round(self.x2)
        self.y2 = round(self.y2)

    @property
    def xc(self):
        return round(super().xc)

    @property
    def yc(self):
        return round(super().yc)

    def move_basis(self, x: int, y: int):
        assert isinstance(x, int) and isinstance(
            y, int
        ), f"Both values must be of type <int>, got x:{type(x)} and y:{type(y)}"
        super().move_basis(x, y)

    def replace_from(self, bbox):
        super().replace_from(bbox)
        self.round_coords()

    def update_from(self, bbox):
        super().update_from(bbox)
        self.round_coords()

    def __repr__(self):
        bbox = f"IntBBox(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2})"
        if text := self.text:
            text = f" - {self.text} ({self.score:.2f})"
        return f"<{bbox}{text}>"
