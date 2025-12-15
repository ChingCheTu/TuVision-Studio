# main.py
import sys
import os
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from widgets.main_window import Ui_TuVision
from config.config import ANALYSIS_CONFIGS
from modules.core.clear import ClearManager
from modules.core.player import VideoPlayer
from modules.core.image_loader import ImageLoader
from modules.core.state_manager import StateManager

class MyMainWindow(QMainWindow, Ui_TuVision):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 初始化狀態與模組
        self.loaded_image = None
        self.analysis_results = {}
        self.analysis_context = None
        self.selected_file = None

        self.state = StateManager()
        self.image_loader = ImageLoader(main_window=self, state=self.state)
        self.player = VideoPlayer(main_window=self, state=self.state)
        self.btnPlatyVid.clicked.connect(self.player.play)
        self.btnPauseVid.clicked.connect(self.player.pause)
        
        # 設定下拉選單與事件綁定
        self.start_analysis_btn.clicked.connect(self.run_analysis)
        self.action_save_result.triggered.connect(self.save_result)
        self.action_load_data.triggered.connect(self.image_loader.load_data)
        self.clear_manager = ClearManager(main_window=self)
        self.action_clear_data.triggered.connect(self.clear_manager.reset_all)
    
    def save_result(self):
        """
        將目前的分析結果自動儲存到 'result' 資料夾中。
        """
        if not self.analysis_context:
            QMessageBox.warning(self, "錯誤", "未設定分析內容 (analysis_context)")
            return

        key = self.analysis_context.get("name")
        if not key or key not in self.analysis_results:
            QMessageBox.warning(self, "錯誤", "沒有可儲存的分析結果")
            return

        # 1. 取得分析結果和格式化器
        result = self.analysis_results.get(key)
        save_formatter = self.analysis_context.get("save_formatter")

        if not callable(save_formatter):
            QMessageBox.critical(self, "錯誤", "未設定有效的儲存格式化器 (save_formatter)")
            return

        # 2. 定義儲存路徑和檔名
        output_dir = "Results"
        
        # 從載入的檔案路徑取得檔名，若無則使用預設值
        if self.selected_file:
            file_basename = os.path.basename(self.selected_file)
            # 移除副檔名，方便命名
            file_name_without_ext = os.path.splitext(file_basename)[0]
        else:
            file_name_without_ext = "no_file"

        # 組合新的檔名，將空格替換為底線
        filename = f"{key.replace(' ', '_')}_{file_name_without_ext}.csv"
        file_path = os.path.join(output_dir, filename)

        try:
            # 3. 檢查並建立儲存資料夾
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # 4. 呼叫格式化器取得要寫入的資料
            rows_to_write = save_formatter(result, self.analysis_context)

            # 5. 將資料寫入 CSV 檔案
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(rows_to_write)
            
            QMessageBox.information(self, "成功", f"結果已成功儲存至:\n{file_path}")
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"儲存檔案時發生錯誤:\n{e}")


    def run_analysis(self):
        selected = self.comboAnalysis.currentText().strip()
        config = ANALYSIS_CONFIGS.get(selected)
        if not config:
            QMessageBox.warning(self, "警告", f"未找到分析設定：{selected}")
            return

        # 建立 context 並帶入「名稱」，避免修改全域設定
        context = dict(config)
        context["name"] = selected
        self.analysis_context = context

        # 從 context 取得函式（保持單一來源）
        func = context.get("func")
        if not callable(func):
            QMessageBox.critical(self, "錯誤", f"分析函式未設定或不可呼叫：{func}")
            return
        try:
            func(self)  # 只呼叫一次
        except Exception as e:
            QMessageBox.critical(self, "錯誤", f"分析執行失敗：{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())