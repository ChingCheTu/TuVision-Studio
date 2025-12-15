# modules/core/clear.py

class ClearManager:
    def __init__(self, main_window):
        self.main = main_window
        self.state = main_window.state

    def reset_all(self):
        # === Step 1: 停止播放 timer（避免多重觸發）===
        if hasattr(self.main.player, "timer") and self.main.player.timer is not None:
            self.main.player.timer.stop()
            self.main.player.timer = None

        # === Step 2: 釋放 VideoCapture 物件（避免舊影片殘留）===
        if self.state.cap is not None:
            self.state.cap.release()
            self.state.cap = None

        # === Step 3: 清除 UI 顯示 ===
        self.main.tabWidgetInput.clear()
        self.main.tabWidgetResult.clear()
        self.main.lineFileName.clear()
        self.main.textResultInfo.clear()
        self.main.lineFrameCount.setText("")

        # === Step 4: 重設主視窗狀態 ===
        self.main.loaded_image = None
        self.main.selected_file = None
        self.main.analysis_results = {}
        self.main.analysis_context = None

        # === Step 5: 清除播放狀態 ===
        self.state.is_video = False
        self.state.is_yuv = False
        self.state.current_frame = 0
        self.state.total_frames = 0
        self.state.yuv_width = 0
        self.state.yuv_height = 0
        self.state.yuv_header = 0

        # === Step 6: ImageLoader 額外重設（如有）===
        if hasattr(self.main.image_loader, "reset") and callable(self.main.image_loader.reset):
            self.main.image_loader.reset()
