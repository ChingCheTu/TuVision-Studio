# modules/core/player.py

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
import cv2
from modules.ui.display import update_image_tabs, update_frame_count_display
from modules.core.yuv_utils import read_nv12_frame_with_header
from modules.ui.components import ImageTabItem

class VideoPlayer:
    def __init__(self, main_window, state):
        self.main = main_window
        self.state = state
        self.timer = None

    def stop(self):
        if self.timer and self.timer.isActive():
            self.timer.stop()
            self.timer = None

    def play(self):
        if not self.state.is_video:
            QMessageBox.information(self.main, "提示", "目前載入的不是影片")
            return

        # === 新增 timer 建立 ===
        if self.timer is None:
            self.timer = QtCore.QTimer()

        if self.state.is_yuv:
            self.timer.timeout.connect(self.play_next_yuv_frame)
        else:
            if self.state.cap is None or not self.state.cap.isOpened():
                QMessageBox.warning(self.main, "錯誤", "影片未載入")
                return
            self.timer.timeout.connect(self.play_next_frame)

        self.timer.start(40)


    def pause(self):
        self.timer.stop()
        if self.timer is not None:
            self.timer.stop()
            self.timer = None

    def play_next_frame(self):
        if self.state.cap.isOpened():
            ret, frame = self.state.cap.read()
            if not ret:
                self.timer.stop()
                return
            self.state.current_frame += 1
            items = [ImageTabItem("Input", frame, "原始輸入影像")]
            update_image_tabs(self.main.tabWidgetInput, items)
            update_frame_count_display(self.main, self.state.current_frame + 1, self.state.total_frames)

    def play_next_yuv_frame(self):
        if self.state.current_frame >= self.state.total_frames:
            self.timer.stop()
            return
        if not self.state.is_yuv:
            print("錯誤：非 YUV 模式不應呼叫 play_next_yuv_frame()")
            self.timer.stop()
            return

        frame = read_nv12_frame_with_header(
            self.main.selected_file,
            self.state.yuv_width,
            self.state.yuv_height,
            self.state.current_frame,
            self.state.yuv_header
        )

        if frame is not None:
            items = [ImageTabItem("Input", frame, "原始輸入影像")]
            update_image_tabs(self.main.tabWidgetInput, items)
            update_frame_count_display(self.main, self.state.current_frame + 1, self.state.total_frames)
            self.state.current_frame += 1
        else:
            self.timer.stop()
