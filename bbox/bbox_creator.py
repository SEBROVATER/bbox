from typing import Sequence, TypeVar

from bbox.types import BBoxKind


class BBoxCreator:
    def __init__(self, coords: Sequence, kind: BBoxKind = "pascal_voc", **kwargs):
        assert kind in (
            "pascal_voc",
            "x1y1x2y2",
            "free_list",
            "tltrbrbl",
            "horizontal_list",
            "x1x2y1y2",
            "coco",
            "x1y1wh",
            "pywinauto",
            "winocr",
        ), f"Unacceptable bbox kind <{kind}>"

        self.is_int = False

        if kind in ("pascal_voc", "x1y1x2y2"):
            self.x1, self.y1, self.x2, self.y2 = coords

        elif kind in ("coco", "x1y1wh"):
            self.x1, self.y1 = coords[:2]
            self.x2, self.y2 = self.x1 + coords[2], self.y1 + coords[3]

        elif kind in ("free_list", "tltrbrbl"):
            (self.x1, self.y1), (x2, y1), (self.x2, self.y2), (x1, y2) = coords

        elif kind in ("horizontal_list", "x1x2y1y2"):
            self.x1, self.x2, self.y1, self.y2 = coords

        elif kind in ("pywinauto",):
            self.x1 = coords.left
            self.y1 = coords.top
            self.x2 = coords.right
            self.y2 = coords.bottom

        elif kind in ("winocr",):
            self.x1, self.y1 = coords["x"], coords["y"]
            self.x2 = self.x1 + coords["width"]
            self.y2 = self.y1 + coords["height"]

        if all(isinstance(coord, int) for coord in (self.x1, self.y1, self.x2, self.y2)):
            self.is_int = True

        self.__dict__.update(kwargs)

    def to_int(self):
        self.is_int = True

        self.x1 = round(self.x1)
        self.x2 = round(self.x2)
        self.y1 = round(self.y1)
        self.y2 = round(self.y2)

    def to_float(self):
        self.is_int = False
        self.x1 = float(self.x1)
        self.x2 = float(self.x2)
        self.y1 = float(self.y1)
        self.y2 = float(self.y2)

    @classmethod
    def create_pascal_voc(cls, coords: Sequence, **kwargs):
        return cls(coords, "pascal_voc", **kwargs)

    @classmethod
    def create_coco(cls, coords: Sequence, **kwargs):
        return cls(coords, "coco", **kwargs)

    @classmethod
    def create_free_list(cls, coords: Sequence, **kwargs):
        return cls(coords, "free_list", **kwargs)

    @classmethod
    def create_horizontal_list(cls, coords: Sequence, **kwargs):
        return cls(coords, "horizontal_list", **kwargs)

    @classmethod
    def create_pywinauto(cls, coords: Sequence, **kwargs):
        return cls(coords, "pywinauto", **kwargs)

    @classmethod
    def create_winocr(cls, coords: Sequence, **kwargs):
        return cls(coords, "winocr", **kwargs)

    @classmethod
    def create_x1y1x2y2(cls, coords: Sequence, **kwargs):
        return cls(coords, "pascal_voc", **kwargs)

    @classmethod
    def create_x1y1wh(cls, coords: Sequence, **kwargs):
        return cls(coords, "coco", **kwargs)

    @classmethod
    def create_tltrbrbl(cls, coords: Sequence, **kwargs):
        return cls(coords, "free_list", **kwargs)

    @classmethod
    def create_x1x2y1y2(cls, coords: Sequence, **kwargs):
        return cls(coords, "horizontal_list", **kwargs)

    def __repr__(self):
        bbox = f"BBox(x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2})"
        return f"<{bbox}>"


BBoxType = TypeVar("BBoxType", bound=BBoxCreator)
