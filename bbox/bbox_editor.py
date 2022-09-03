from bbox.bbox_getter import BBoxGetter


class BBoxEditor(BBoxGetter):
    def move_basis(self, x: int | float, y: int | float):
        if self.is_int:
            x = round(x)
            y = round(y)

        self.x1 += x
        self.x2 += x
        self.y1 += y
        self.y2 += y

    def zero_basis(self):
        self.x2 = self.w
        self.y2 = self.h
        self.x1 = 0
        self.y1 = 0

    def multiply_by(self, value: int | float):
        self.x1 = self.x1 * value
        self.y1 = self.y1 * value
        self.x2 = self.x2 * value
        self.y2 = self.y2 * value
        if self.is_int:
            self.to_int()

    def divide_by(self, value: int | float):
        self.x1 = self.x1 / value
        self.y1 = self.y1 / value
        self.x2 = self.x2 / value
        self.y2 = self.y2 / value
        if self.is_int:
            self.to_int()

    def replace_from(self, bbox):
        if self.is_int and not bbox.is_int:
            self.to_float()

        self.x1 = bbox.x1
        self.y1 = bbox.y1
        self.x2 = bbox.x2
        self.y2 = bbox.y2

    def update_from(self, bbox):
        if self.is_int and not bbox.is_int:
            bbox.to_int()

        self.x1 = min(self.x1, bbox.x1)
        self.y1 = min(self.y1, bbox.y1)
        self.x2 = max(self.x2, bbox.x2)
        self.y2 = max(self.y2, bbox.y2)
