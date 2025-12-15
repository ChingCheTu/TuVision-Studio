import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox
from modules.ui.display import update_image_tabs
from modules.ui.components import ImageTabItem
from modules.analysis.select_roi import select_roi_scaled

def run_grayscale_analysis(main_window):
    if main_window.loaded_image is None:
        QMessageBox.warning(main_window, "錯誤", "請先載入影像")
        return

    # 從 main.py 塞進來的 analysis_context 取得名稱與 formatter
    config = getattr(main_window, "analysis_context", {}) or {}
    key = config.get("name")
    if not key:
        QMessageBox.critical(main_window, "錯誤", "分析名稱遺失（analysis_context['name'] 未設定）")
        return
    
    # 清理舊結果 & UI
    main_window.analysis_results.pop(key, None)
    main_window.tabWidgetResult.clear()
    main_window.textResultInfo.clear()

    image_bgr = main_window.loaded_image.copy()
    roi_box = select_roi_scaled(image_bgr)

    if roi_box:
        x, y, w, h = roi_box

    else:
        print("使用者取消了 ROI 選擇。")
    # roi_box = cv2.selectROI("Select ROI", image_bgr, fromCenter=False)
    # cv2.destroyAllWindows()

    x, y, w, h = roi_box
    if w == 0 or h == 0:
        QMessageBox.warning(main_window, "錯誤", "未選取有效 ROI")
        return

    # 將 ROI 區域從 BGR 轉換為灰階
    roi = image_bgr[y:y+h, x:x+w]
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # 顯示帶有 ROI 框的原始影像
    image_with_box = image_bgr.copy()
    cv2.rectangle(image_with_box, (x, y), (x + w, y + h), (0, 0, 255), 2)

    update_image_tabs(main_window.tabWidgetInput, [
        ImageTabItem("Input", image_with_box, "原始輸入影像")
    ])
    update_image_tabs(main_window.tabWidgetResult, [
        ImageTabItem("ROI", roi_gray, "選取區域")
    ])

    # 計算 ROI 的平均灰階值
    avg_grayscale = float(np.mean(roi_gray))

    # 更新 result 字典
    result = {
        "Grayscale": avg_grayscale,
        "ROI": (int(x), int(y), int(w), int(h)),
    }

    # 以分析名稱作為 key 存入最新結果
    main_window.analysis_results[key] = result

    # 處理顯示，不再理會 display_formatter
    display_fmt = config.get("display_formatter")
    if callable(display_fmt):
        text = display_fmt(result, config)
    else:
        # 最後保底顯示
        text = (
            f"[Analysis] {key}\n"
            f"Avg Grayscale: {int(avg_grayscale)}"
        )

    main_window.textResultInfo.setPlainText(text)