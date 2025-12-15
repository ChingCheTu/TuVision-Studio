def awb_display_format(result: dict, context: dict = None) -> str:
    mode_name = context.get("name") if context else "Unknown"
    return (
        f"[Analysis Mode] {mode_name}\n"
        f"R: {int(round(result.get('R', 0)))}\n"
        f"G: {int(round(result.get('G', 0)))}\n"
        f"B: {int(round(result.get('B', 0)))}\n"
        f"R / G: {result.get('R/G', 0):.2f}\n"
        f"B / G: {result.get('B/G', 0):.2f}"
    )

def grayscale_analysis_display_format(result: dict, context: dict = None) -> str:
    """
    將灰階分析結果格式化為顯示用的多行字串。
    """
    # 取得分析模式名稱，若無則使用預設值
    mode_name = context.get("name", "Grayscale Analysis") if context else "Grayscale Analysis"
    
    # 從 result 字典中取得灰階值和 ROI 位置
    avg_grayscale = result.get('Grayscale', 0)
    roi_coords = result.get('ROI', (0, 0, 0, 0))

    return (
        f"[Analysis Mode] {mode_name}\n"
        f"Avg Grayscale: {int(avg_grayscale)}\n"
        f"ROI (x, y, w, h): {roi_coords[0]}, {roi_coords[1]}, {roi_coords[2]}, {roi_coords[3]}"
    )