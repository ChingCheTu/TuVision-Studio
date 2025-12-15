import cv2
def select_roi_scaled(original_image, max_width=1280, max_height=720):
    """
    載入圖片並以縮小的方式顯示，讓使用者選擇 ROI，
    最後回傳原始圖片上的 ROI 座標。

    Args:
        image_path (str): 圖片路徑。
        max_width (int): 顯示視窗的最大寬度。
        max_height (int): 顯示視窗的最大高度。

    Returns:
        tuple: (x, y, w, h) 在原始圖片上的 ROI 座標。
               如果使用者取消選擇，則回傳 None。
    """
    # 載入原始圖片
    # original_image = cv2.imread(image_path)
    # if original_image is None:
    #     print(f"錯誤：無法載入圖片 {image_path}")
    #     return None

    h, w, _ = original_image.shape

    # 判斷是否需要縮小，並計算縮放比例
    if w > max_width or h > max_height:
        scale_ratio = min(max_width / w, max_height / h)
        display_w = int(w * scale_ratio)
        display_h = int(h * scale_ratio)
        resized_image = cv2.resize(original_image, (display_w, display_h), interpolation=cv2.INTER_AREA)
    else:
        scale_ratio = 1.0
        resized_image = original_image

    # print("請在彈出的視窗中選擇 ROI 並按下 Enter 或空白鍵。")
    # print("若要取消，請按下 'c' 鍵。")
    
    # 在縮小後的圖片上選擇 ROI
    roi_box_scaled = cv2.selectROI("Select ROI", resized_image, fromCenter=False)
    cv2.destroyAllWindows()

    if roi_box_scaled == (0, 0, 0, 0): # cv2.selectROI 取消選擇時會回傳 (0, 0, 0, 0)
        return None

    # 將 ROI 座標轉換回原始圖片的尺寸
    x_scaled, y_scaled, w_scaled, h_scaled = roi_box_scaled
    
    x_orig = int(x_scaled / scale_ratio)
    y_orig = int(y_scaled / scale_ratio)
    w_orig = int(w_scaled / scale_ratio)
    h_orig = int(h_scaled / scale_ratio)
    
    return (x_orig, y_orig, w_orig, h_orig)