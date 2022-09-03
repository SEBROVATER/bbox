from typing import Literal

BBoxKind = Literal[
    "free_list",
    "tltrbrbl",
    "horizontal_list",
    "x1x2y1y2",
    "pascal_voc",
    "x1y1x2y2",
    "coco",
    "x1y1wh",
    "pywinauto",
    "winocr",
]
