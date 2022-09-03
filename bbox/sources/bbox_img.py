from abc import ABC

import cv2
import numpy as np

from ..cv_utils import resize


class BBoxImg(ABC):
    def show(self, img: np.ndarray, text: str = ""):
        img = img.copy()
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        cv2.rectangle(
            img, (round(self.x1), round(self.y1)), (round(self.x2), round(self.y2)), (0, 255, 0)
        )
        cv2.putText(
            img,
            text,
            (round(self.x1), round(self.y1) + 10),
            cv2.FONT_ITALIC,
            0.5,
            (0, 0, 255),
            2,
        )

        cv2.imshow("temp", resize(img, height=800))
        cv2.waitKey(0)
        cv2.destroyWindow("temp")

    def crop(self, img: np.ndarray):
        img = img.copy()
        img = img[self.y1 : self.y2, self.x1 : self.x2]

        return img
