from typing import Union
import numpy as np
from dataclasses import dataclass
from PyQt5 import QtGui
@dataclass
class ImageTabItem:
    title: str
    image: Union[np.ndarray, QtGui.QImage]
    info: str = ""