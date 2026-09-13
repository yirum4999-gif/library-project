from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout


class KioskDialog(QDialog):
    """키오스크 공용 알림 다이얼로그의 기반 클래스."""
    def __init__(self, title, message, parent=None):
        super().__init__(parent)
        self.setModal(True)
        self.setMinimumSize(640, 360)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(42, 36, 42, 36)
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 30px; font-weight: bold; color: #172554;")
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("font-size: 22px; color: #334155; padding: 20px;")
        layout.addWidget(title_label)
        layout.addWidget(message_label, 1)
        self.button_layout = QHBoxLayout()
        layout.addLayout(self.button_layout)
        self.setStyleSheet("QDialog { background: #F8FAFC; }")

    def add_button(self, text, role):
        button = QPushButton(text)
        button.setMinimumHeight(76)
        button.setStyleSheet("font-size: 23px; font-weight: bold; border-radius: 14px; background: #2563EB; color: white;")
        button.clicked.connect(role)
        self.button_layout.addWidget(button)


class InfoDialog(KioskDialog):
    def __init__(self, title, message, parent=None):
        super().__init__(title, message, parent)
        self.add_button("確認", self.accept)


class ConfirmDialog(KioskDialog):
    def __init__(self, title, message, parent=None):
        super().__init__(title, message, parent)
        self.add_button("取消", self.reject)
        self.add_button("確認", self.accept)
