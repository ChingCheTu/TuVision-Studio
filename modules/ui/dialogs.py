from PyQt5.QtWidgets import (
    QDialog, QDialogButtonBox, QVBoxLayout, QFormLayout,
    QLineEdit
)

class YUVParameterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("輸入 YUV 參數")
        self.setModal(True)

        # 正確的寫法：直接定義為 self.width_input，而不是 self.state.width_input
        self.width_input = QLineEdit("1280")
        self.height_input = QLineEdit("720")
        self.header_input = QLineEdit("64")

        form_layout = QFormLayout()
        form_layout.addRow("寬度 (px)：", self.width_input)
        form_layout.addRow("高度 (px)：", self.height_input)
        form_layout.addRow("Header 大小 (bytes)：", self.header_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(buttons)
        self.setLayout(layout)


    def get_values(self):
        try:
            width = int(self.width_input.text())
            height = int(self.height_input.text())
            header = int(self.header_input.text())
            return width, height, header
        except ValueError:
            return None

def get_yuv_parameters(parent=None):
    dialog = YUVParameterDialog(parent)
    if dialog.exec_() == QDialog.Accepted:
        values = dialog.get_values()
        if values:
            return values
    return None
