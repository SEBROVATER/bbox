from bbox.bbox_creator import BBoxCreator


class BBoxGetter(BBoxCreator):
    def get_pascal_voc(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def get_x1y1x2y2(self):
        return self.get_pascal_voc()

    def get_coco(self):
        return (self.x1, self.y1, self.w, self.h)

    def get_x1y1wh(self):
        return self.get_coco()

    def get_free_list(self):
        return (self.tl, self.tr, self.br, self.bl)

    def get_tltrbrbl(self):
        return self.get_free_list()

    def get_horizontal_list(self):
        return (self.x1, self.x2, self.y1, self.y2)

    def get_x1x2y1y2(self):
        return self.get_horizontal_list()

    @property
    def w(self):
        return self.x2 - self.x1

    @property
    def h(self):
        return self.y2 - self.y1

    @property
    def xc(self):
        center = (self.x1 + self.x2) / 2
        if self.is_int:
            center = round(center)
        return center

    @property
    def yc(self):
        center = (self.y1 + self.y2) / 2
        if self.is_int:
            center = round(center)
        return center

    @property
    def area(self):
        return self.w * self.h

    @property
    def center(self):
        return (self.xc, self.yc)

    @property
    def tl(self):
        return (self.x1, self.y1)

    @property
    def tr(self):
        return (self.x2, self.y1)

    @property
    def br(self):
        return (self.x2, self.y2)

    @property
    def bl(self):
        return (self.x1, self.y2)
