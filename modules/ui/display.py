# modules/ui/display.py
from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np
import cv2
from modules.ui.components import ImageTabItem

def update_frame_count_display(main_window, current_frame: int, total_frames: int):
    """
    更新主視窗中的 Frame Count 顯示欄位為「目前 Frame / 總 Frame」格式。
    若僅有 1 張 frame，則只顯示「Frame: N」。

    Args:
        main_window: 主視窗物件 (MyMainWindow 實例)
        current_frame (int): 目前的 frame 編號（通常從 1 起算）
        total_frames (int): 總 frame 數
    """
    if hasattr(main_window, 'lineFrameCount'):
        if total_frames <= 1:
            text = f"Frame: {total_frames}"
        else:
            text = f"Frame: {current_frame} / {total_frames}"
        main_window.lineFrameCount.setText(text)
def update_image_tabs(tab_widget, tab_data_list, clear_tabs=True):
    """
    更新指定 tab_widget 中的影像頁籤。

    參數：
        tab_widget (QTabWidget): 要更新的 tab 視圖。
        tab_data_list (list): 包含 ImageTabItem 的清單。
        clear_tabs (bool): 是否先清空原有的 tab，預設為 True。
    """
    if tab_widget is None or not isinstance(tab_data_list, list):
        return

    if clear_tabs:
        tab_widget.clear()

    for data in tab_data_list:
        if not isinstance(data, ImageTabItem):
            continue

        if data.image is None:
            continue

        # 轉換為 QImage
        if isinstance(data.image, np.ndarray):
            q_image = image_to_qimage(data.image)
        elif isinstance(data.image, QtGui.QImage):
            q_image = data.image
        else:
            continue

        # 顯示於 QGraphicsView
        view = qimage_to_view(q_image)
        index = tab_widget.addTab(view, data.title)
        tab_widget.setTabToolTip(index, data.info)

def image_to_qimage(image: np.ndarray) -> QtGui.QImage:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, ch = image_rgb.shape
    bytes_per_line = ch * w
    return QtGui.QImage(image_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

def qimage_to_view(qimage: QtGui.QImage, width=469, height=271) -> QtWidgets.QGraphicsView:
    pixmap = QtGui.QPixmap.fromImage(qimage).scaled(
        width, height,
        QtCore.Qt.KeepAspectRatio,
        QtCore.Qt.SmoothTransformation
    )
    scene = QtWidgets.QGraphicsScene()
    scene.addPixmap(pixmap)
    view = QtWidgets.QGraphicsView()
    view.setScene(scene)
    view.setFixedSize(width + 2, height + 2)
    view.setAlignment(QtCore.Qt.AlignCenter)
    return view

