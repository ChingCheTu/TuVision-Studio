def awb_save_format(result: dict, context: dict = None) -> list:
    """
    將 AWB 分析結果格式化為 CSV 寫入所需的二維列表。
    """
    return [
        ['Items', 'Value'],
        ['R', int(round(result.get('R', 0)))],
        ['G', int(round(result.get('G', 0)))],
        ['B', int(round(result.get('B', 0)))],
        ['R/G', f"{result.get('R/G', 0):.2f}"], # 使用 f-string 格式化
        ['B/G', f"{result.get('B/G', 0):.2f}"], # 使用 f-string 格式化
    ]

def grayscale_analysis_save_format(result: dict, context: dict = None) -> list:
    """
    將灰階分析結果格式化為 CSV 寫入所需的二維列表。
    """
    # 從 result 字典中取得灰階值和 ROI 位置
    avg_grayscale = result.get('Grayscale', 0)
    roi_coords = result.get('ROI', (0, 0, 0, 0))
    
    return [
        ['Items', 'Value'],
        ['Avg Grayscale', f"{int(avg_grayscale)}"],
        ['ROI (x, y, w, h)', f"{roi_coords[0]}, {roi_coords[1]}, {roi_coords[2]}, {roi_coords[3]}"]
    ]