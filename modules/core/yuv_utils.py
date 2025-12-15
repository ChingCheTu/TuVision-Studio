# modules/core/yuv_utils.py
import os
import numpy as np
import cv2

def read_nv12_frame_with_header(yuv_path, width, height, frame_idx, header_size=64):
    """
    讀取帶有 header 的 NV12 格式 YUV 檔案中指定 frame，轉換為 BGR 格式影像。

    Parameters:
        yuv_path (str): 檔案路徑
        width (int): 寬度
        height (int): 高度
        frame_idx (int): 欲讀取的 frame 編號（從 0 開始）
        header_size (int): 每幀開頭的 header 大小（bytes）

    Returns:
        np.ndarray 或 None: 若成功則回傳 BGR 影像，否則為 None
    """
    if not os.path.exists(yuv_path):
        print(f"檔案不存在：{yuv_path}")
        return None

    y_size = width * height
    uv_size = (width // 2) * (height // 2) * 2
    frame_size = header_size + y_size + uv_size

    try:
        with open(yuv_path, 'rb') as f:
            f.seek(frame_idx * frame_size + header_size)
            y_raw = f.read(y_size)
            uv_raw = f.read(uv_size)

            if len(y_raw) < y_size or len(uv_raw) < uv_size:
                print(f"frame {frame_idx} 資料不足")
                return None

            y = np.frombuffer(y_raw, dtype=np.uint8).reshape((height, width))
            uv = np.frombuffer(uv_raw, dtype=np.uint8).reshape((height // 2, width))
            nv12 = np.vstack((y, uv))

            try:
                bgr = cv2.cvtColor(nv12, cv2.COLOR_YUV2BGR_NV12)
                return bgr
            except cv2.error as e:
                print(f"YUV 轉 BGR 失敗：{e}")
                return None

    except Exception as e:
        print(f"讀取 NV12 發生錯誤: {e}")
        return None
