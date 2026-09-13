from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                               QStackedWidget, QVBoxLayout, QWidget)

from view.components import ActionCard, BarcodeInput, ConfirmCancelCard, ManualInputCard


class LoginPage(QWidget):
    """로그인 흐름의 루트. 하위 세 화면은 LoginPresenter만 전환한다."""
    login_success = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stack = QStackedWidget()
        self.scan_page = ScanLoginPage()
        self.manual_page = ManualInputPage()
        self.pin_page = PinPage()
        for page in (self.scan_page, self.manual_page, self.pin_page):
            self.stack.addWidget(page)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.stack)


class ScanLoginPage(QWidget):
    """별도 바코드 페이지를 없앤 로그인 첫 화면으로 통합한 화면."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.barcode_input = BarcodeInput(self)
        self.manual_input_card = ManualInputCard(self)
        title = QLabel("会員証のバーコードをスキャンしてください")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 38px; font-weight: bold; color: #172554;")
        guide = QLabel("スキャナーに会員証をかざしてください")
        guide.setAlignment(Qt.AlignmentFlag.AlignCenter)
        guide.setStyleSheet("font-size: 20px; color: #475569;")
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setMinimumSize(540, 270)
        self.image_label.setStyleSheet("background: #E0F2FE; border: 3px dashed #38BDF8; border-radius: 24px; color: #0369A1; font-size: 22px;")
        image_path = Path(__file__).parents[2] / "resource" / "img" / "member_barcode_scan.png"
        pixmap = QPixmap(str(image_path))
        if pixmap.isNull():
            self.image_label.setText("画像を配置してください\nresource/img/member_barcode_scan.png")
        else:
            self.image_label.setPixmap(pixmap.scaled(520, 250, Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation))
        layout = QVBoxLayout(self)
        layout.setContentsMargins(80, 50, 80, 50)
        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(12)
        layout.addWidget(guide)
        layout.addSpacing(28)
        layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(28)
        layout.addWidget(self.manual_input_card, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.barcode_input)
        layout.addStretch()


class ManualInputPage(QWidget):
    member_submitted = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        title = QLabel("会員番号を入力してください")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: bold; color: #172554;")
        self.member_input = QLineEdit()
        self.member_input.setPlaceholderText("会員番号")
        self.member_input.setMaxLength(30)
        self.member_input.setMinimumHeight(76)
        self.member_input.setStyleSheet("font-size: 28px; padding: 12px; border: 2px solid #94A3B8; border-radius: 14px;")
        self.action_card = ConfirmCancelCard()
        self.action_card.confirmed.connect(lambda: self.member_submitted.emit(self.member_input.text().strip()))
        layout = QVBoxLayout(self)
        layout.setContentsMargins(180, 80, 180, 80)
        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(40)
        layout.addWidget(self.member_input)
        layout.addSpacing(24)
        layout.addWidget(self.action_card)
        layout.addStretch()


class PinPage(QWidget):
    pin_submitted = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pin = ""
        title = QLabel("暗証番号を入力してください")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: bold; color: #172554;")
        self.pin_display = QLineEdit()
        self.pin_display.setReadOnly(True)
        self.pin_display.setEchoMode(QLineEdit.EchoMode.Password)
        self.pin_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pin_display.setMinimumHeight(74)
        self.pin_display.setStyleSheet("font-size: 30px; letter-spacing: 10px; border: 2px solid #94A3B8; border-radius: 14px;")
        keypad = QGridLayout()
        for number in range(1, 10):
            keypad.addWidget(self._key(str(number)), (number - 1) // 3, (number - 1) % 3)
        keypad.addWidget(self._key("0"), 3, 0)
        keypad.addWidget(self._key("削除"), 3, 1)
        keypad.addWidget(self._key("全消去"), 3, 2)
        self.action_card = ConfirmCancelCard()
        self.action_card.confirmed.connect(lambda: self.pin_submitted.emit(self.pin))
        layout = QVBoxLayout(self)
        layout.setContentsMargins(210, 50, 210, 50)
        layout.addWidget(title)
        layout.addSpacing(22)
        layout.addWidget(self.pin_display)
        layout.addSpacing(20)
        layout.addLayout(keypad)
        layout.addSpacing(14)
        layout.addWidget(self.action_card)

    def _key(self, text):
        card = ActionCard(text, "#334155" if not text.isdigit() else "#2563EB", 150, 78)
        card.clicked.connect(lambda: self._press(text))
        return card

    def _press(self, text):
        if text == "削除":
            self.pin = self.pin[:-1]
        elif text == "全消去":
            self.pin = ""
        elif len(self.pin) < 12:
            self.pin += text
        self.pin_display.setText(self.pin)

    def clear(self):
        self.pin = ""
        self.pin_display.clear()
