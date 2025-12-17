# modules/ui/display.py
from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np
import cv2
from modules.ui.components import ImageTabItem

# -----------------------------------------------------------
# 新增一個自定義類別：會自動縮放圖片的 GraphicsView
# -----------------------------------------------------------
class ResponsiveGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        # 開啟平滑縮放 (對 IQ 分析很重要，避免鋸齒)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        
        # 隱藏捲軸 (因為我們會做 Fit In View，不需要捲軸)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        # [新增] 設定背景顏色為深灰色 (RGB: 30, 30, 30)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        
        # [可選] 去掉邊框，讓圖片跟背景融合得更好
        self.setStyleSheet("border: 0px;")
        
        # 設定對齊
        self.setAlignment(QtCore.Qt.AlignCenter)

    def resizeEvent(self, event):
        """
        當視窗大小改變時，自動觸發此事件
        """
        super().resizeEvent(event)
        if self.scene():
            # 關鍵指令：將 Scene (圖片) 縮放至 View (視窗) 的大小
            # KeepAspectRatio: 保持長寬比
            self.fitInView(self.scene().sceneRect(), QtCore.Qt.KeepAspectRatio)


# -----------------------------------------------------------
# 原有的函式 (未修改)
# -----------------------------------------------------------
def update_frame_count_display(main_window, current_frame: int, total_frames: int):
    if hasattr(main_window, 'lineFrameCount'):
        if total_frames <= 1:
            text = f"Frame: {total_frames}"
        else:
            text = f"Frame: {current_frame} / {total_frames}"
        main_window.lineFrameCount.setText(text)

# -----------------------------------------------------------
# 修改後的 update_image_tabs
# -----------------------------------------------------------
def update_image_tabs(tab_widget, tab_data_list, clear_tabs=True):
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

        # 顯示於 ResponsiveGraphicsView (修改處)
        view = qimage_to_view(q_image)
        index = tab_widget.addTab(view, data.title)
        tab_widget.setTabToolTip(index, data.info)

def image_to_qimage(image: np.ndarray) -> QtGui.QImage:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, ch = image_rgb.shape
    bytes_per_line = ch * w
    return QtGui.QImage(image_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

# -----------------------------------------------------------
# 大幅修改後的 qimage_to_view
# -----------------------------------------------------------
def qimage_to_view(qimage: QtGui.QImage) -> QtWidgets.QGraphicsView:
    """
    將 QImage 放入我們自定義的 ResponsiveGraphicsView 中
    """
    # 1. 建立原始大小的 Pixmap (不要在這裡縮放，保留原始解析度)
    pixmap = QtGui.QPixmap.fromImage(qimage)
    
    # 2. 建立場景並加入圖片
    scene = QtWidgets.QGraphicsScene()
    scene.addPixmap(pixmap)
    
    # 3. 使用自定義的 View，而不是原本的 QGraphicsView
    # 也不要設定 setFixedSize，讓 Layout 決定它的大小
    view = ResponsiveGraphicsView(scene)
    
    # 4. 這裡不需要再手動 scaled 或 setFixedSize 了
    
    return view