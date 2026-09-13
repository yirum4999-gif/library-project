from view.components import ActionCard
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget

class HomePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._create_widget()
        self._create_layout()

    def _create_widget(self):
        """내부 카드 컴포넌트 생성"""
        self.loan_card = ActionCard("図書貸出", "#2563EB", 390, 300, "会員認証後に本をスキャン")
        self.receive_card = ActionCard("図書返却", "#059669", 390, 300, "本のバーコードをスキャン")

    def _create_layout(self):
        """레이아웃 구조 생성 및 배치"""
        # 1. 메인 수직 레이아웃 (상하 중앙 정렬용)
        self.main_layout = QVBoxLayout(self)
        title = QLabel("図書館セルフサービス")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 42px; font-weight: bold; color: #172554;")

        # 2. 카드들을 담을 수평 레이아웃 컨테이너
        self.contents = QWidget()
        self.contents_layout = QHBoxLayout(self.contents)
        self.contents_layout.setSpacing(80)

        # 위젯 배치
        self.contents_layout.addWidget(self.loan_card)
        self.contents_layout.addWidget(self.receive_card)

        # 정중앙 배치를 위한 Stretch 조합
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(title)
        self.main_layout.addSpacing(36)
        self.main_layout.addWidget(
            self.contents, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.main_layout.addStretch(1)
