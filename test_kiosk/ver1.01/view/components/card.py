from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QMouseEvent
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout


class ActionCard(QFrame):
    """터치로 누를 수 있는 공용 카드 컴포넌트."""

    clicked = Signal()

    def __init__(self, title, color_theme="#2563EB", card_w_size=320,
                 card_h_size=None, subtitle=None, parent=None):
        super().__init__(parent)
        self.setObjectName("actionCard")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(card_w_size, card_h_size or card_w_size)
        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont("Yu Gothic UI", 27, QFont.Weight.Bold))
        self.title.setWordWrap(True)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.addStretch()
        layout.addWidget(self.title)
        if subtitle:
            hint = QLabel(subtitle)
            hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hint.setWordWrap(True)
            hint.setStyleSheet("font-size: 16px; color: #EAF2FF;")
            layout.addSpacing(12)
            layout.addWidget(hint)
        layout.addStretch()
        self.setStyleSheet(f"""
            QFrame#actionCard {{ background: {color_theme}; border: 0; border-radius: 24px; }}
            QFrame#actionCard:hover {{ background: {color_theme}; border: 4px solid #FFFFFF; }}
            QLabel {{ color: white; }}
        """)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class ManualInputCard(ActionCard):
    """회원번호 수기 입력으로 진입하는 로그인 전용 카드."""

    def __init__(self, parent=None):
        super().__init__("会員番号を入力", "#D97706", 330, 250,
                         "バーコードを読み取れない場合", parent)


class ConfirmCancelCard(QFrame):
    """확인/취소가 반복되는 화면을 위한 완성형 카드 컴포넌트."""

    confirmed = Signal()
    cancelled = Signal()

    def __init__(self, confirm_text="確認", cancel_text="取消", parent=None):
        super().__init__(parent)
        self.setObjectName("confirmCancelCard")
        self.setFixedHeight(108)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        self.cancel_label = QLabel(cancel_text)
        self.confirm_label = QLabel(confirm_text)
        for label in (self.cancel_label, self.confirm_label):
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setFont(QFont("Yu Gothic UI", 22, QFont.Weight.Bold))
            label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.cancel_label.setObjectName("cancel")
        self.confirm_label.setObjectName("confirm")
        layout.addWidget(self.cancel_label, 1)
        layout.addSpacing(12)
        layout.addWidget(self.confirm_label, 1)
        self.setStyleSheet("""
            QFrame#confirmCancelCard { background: transparent; }
            QLabel { color: white; border-radius: 16px; }
            QLabel#cancel { background: #64748B; }
            QLabel#confirm { background: #2563EB; }
            QLabel#cancel:hover, QLabel#confirm:hover { border: 3px solid white; }
        """)

    def mousePressEvent(self, event):
        child = self.childAt(event.position().toPoint())
        if child is self.confirm_label:
            self.confirmed.emit()
        elif child is self.cancel_label:
            self.cancelled.emit()
        super().mousePressEvent(event)
