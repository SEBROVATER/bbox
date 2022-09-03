from typing import Any

import cv2
import imutils
import numpy as np

from bbox.bbox_creator import BBoxCreator


class BBoxImg(BBoxCreator):
    def show(self, img: np.ndarray, text: str = ""):
        img = img.copy()
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        cv2.rectangle(img, (round(self.x1), round(self.y1)), (round(self.x2), round(self.y2)), (0, 255, 0))
        cv2.putText(
            img,
            text,
            (round(self.x1), round(self.y1) + 10),
            cv2.FONT_ITALIC,
            0.5,
            (0, 0, 255),
            2,
        )

        cv2.imshow("temp", imutils.resize(img, height=800))
        cv2.waitKey(0)
        cv2.destroyWindow("temp")

    def crop(self, img: np.ndarray):
        img = img.copy()
        img = img[self.y1 : self.y2, self.x1 : self.x2]

        return img

    def cut_extra(self, basis_bbox_or_img: Any):
        basis = basis_bbox_or_img

        self.x1 = max((0, self.x1))
        self.y1 = max((0, self.y1))

        if isinstance(basis, np.ndarray):
            self.x2 = min((basis.shape[1], self.x2))
            self.y2 = min((basis.shape[0], self.y2))
        else:
            self.x2 = min((basis.x2, self.x2))
            self.y2 = min((basis.y2, self.y2))
