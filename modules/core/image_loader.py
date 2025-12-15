# modules/core/image_loader.py
import os
import cv2
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from .yuv_utils import read_nv12_frame_with_header
from modules.ui.dialogs import get_yuv_parameters  # 自訂 YUV 輸入對話框
from modules.ui.components import ImageTabItem
from modules.ui.display import update_frame_count_display, update_image_tabs

class ImageLoader:
    def __init__(self, main_window, state):
        self.main = main_window      # 主視窗參考
        self.state = state           # 統一管理影像狀態

    def load_data(self):

        if hasattr(self.main, "player"):
            self.main.player.stop()
        file_path, _ = QFileDialog.getOpenFileName(
            self.main, "\u9078\u64c7\u5716\u7247\u6216\u5f71\u7247", "",
            "Image or Video Files (*.png *.jpg *.bmp *.mp4 *.avi *.mov *.yuv)"
        )
        if not file_path:
            return

        self.main.lineFileName.setText(os.path.basename(file_path))
        self.main.selected_file = file_path
        file_ext = os.path.splitext(file_path)[1].lower()

        if file_ext in ['.png', '.jpg', '.jpeg', '.bmp']:
            self._load_image_file(file_path)
        elif file_ext in ['.mp4', '.avi', '.mov']:
            self._load_video_file(file_path)
        elif file_ext == '.yuv':
            self._load_yuv_file(file_path)
        else:
            QMessageBox.warning(self.main, "\u932f\u8aa4", "\u4e0d\u652f\u63f4\u7684\u6a94\u6848\u683c\u5f0f")

    def _load_image_file(self, file_path):
        self.state.is_video = False
        self.state.is_yuv = False

        image = cv2.imread(file_path)
        if image is None:
            QMessageBox.warning(self.main, "\u932f\u8aa4", "\u8f09\u5165\u5716\u7247\u5931\u6557")
            return

        self.main.loaded_image = image.copy()
        self.state.total_frames = 1
        items = [ImageTabItem("Input", image, "\u539f\u59cb\u8f38\u5165\u5f71\u50cf")]
        update_image_tabs(self.main.tabWidgetInput, items)
        update_frame_count_display(self.main, self.state.current_frame, self.state.total_frames)

    def _load_video_file(self, file_path):
        self.state.is_video = True
        self.state.is_yuv = False
        self.state.cap = cv2.VideoCapture(file_path)

        if not self.state.cap.isOpened():
            QMessageBox.warning(self.main, "錯誤", "無法開啟影片")
            return

        self.state.total_frames = int(self.state.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.state.current_frame = 0
        self.state.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        ret, frame = self.state.cap.read()
        if ret:
            self.state.loaded_image = frame.copy()

            items = [ImageTabItem("Input", frame, "原始輸入影像")]
            update_image_tabs(self.main.tabWidgetInput, items)

            update_frame_count_display(
                self.main,
                self.state.current_frame + 1,
                self.state.total_frames
            )
        else:
            QMessageBox.warning(self.main, "錯誤", "讀取第一幀失敗")

    def _load_yuv_file(self, file_path):
        self.state.is_video = False
        self.state.is_yuv = True

        width, height, header = get_yuv_parameters(self.main)
        if width is None or height is None or header is None:
            return

        self.state.yuv_width = width
        self.state.yuv_height = height
        self.state.yuv_header = header

        y_size = width * height
        uv_size = (width // 2) * (height // 2) * 2
        frame_size = header + y_size + uv_size
        total_bytes = os.path.getsize(file_path)

        self.state.total_frames = total_bytes // frame_size
        self.state.current_frame = 0

        frame = read_nv12_frame_with_header(file_path, width, height, 0, header)
        if frame is not None:
            self.main.loaded_image = frame.copy()
            items = [ImageTabItem("Input", frame, "原始輸入影像")]
            update_image_tabs(self.main.tabWidgetInput, items)
            update_frame_count_display(self.main, self.state.current_frame + 1, self.state.total_frames)
            self.state.is_video = self.state.total_frames > 1
        else:
            QMessageBox.warning(self.main, "錯誤", "YUV 解析失敗")
            self.state.is_video = False
            self.state.is_yuv = False