from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Signal

class BarcodeInput(QLineEdit):
    """바코드 입력 전용 QLineEdit 커스텀 컴포넌트"""

    barcodeEntered = Signal(str)  # 바코드 입력 완료 시그널

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(1, 1)
        self.returnPressed.connect(self._on_barcode_entered)
        self.setFocus()
        self.setStyleSheet("""
            QLineEdit { 
                border: none;
                background: transparent;
                color: transparent;
                padding: 0px;
                margin: 0px;
            }
        """)
    
    def _on_barcode_entered(self):
        """바코드 입력 완료 시그널 발생"""
        barcode = self.text().strip()
        if barcode:
            self.barcodeEntered.emit(barcode)

        self.clear()
        self.setFocus()