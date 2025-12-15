# modules/core/state_manager.py

class StateManager:
    def __init__(self):
        self.reset()

    def reset(self):
        # === 載入狀態 ===
        self.cap = None                 # cv2.VideoCapture，用於影片播放
        self.is_video = False          # 是否為影片類型
        self.is_yuv = False            # 是否為 YUV 格式
        self.yuv_width = 0             # YUV 寬度
        self.yuv_height = 0            # YUV 高度
        self.yuv_header = 0            # YUV header 大小（bytes）

        # === Frame 狀態 ===
        self.current_frame = 0         # 當前顯示的 frame 編號（0-based）
        self.total_frames = 0          # 總 frame 數量

        # === 分析狀態（若有需要）===
        self.analysis_context = None   # 當前分析模式（例如 AWB, SplitRGB 等）
        self.analysis_results = {}     # 分析結果（可選，若你把它也從 main 搬來）

        # （如需進一步擴充，可考慮新增 loading flag、timer 狀態、error flag 等）

