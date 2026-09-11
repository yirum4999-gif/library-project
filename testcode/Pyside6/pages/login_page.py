from card import ActionCard
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
    QPushButton
)

import requests

BASE_URL = "http://192.168.0.98:8090/test28/api/"

class LoginPage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._create_widget()
        self._create_layout()

    def _create_widget(self):
        """내부 카드 컴포넌트 생성"""
        self.barcode_card = ActionCard("バーコード入力", "#DE8517", 300,400)
        self.manual_input_card = ActionCard("手入力", "#DE8517", 300,400)

    def _create_layout(self):

        self.main_layout=QVBoxLayout(self)
        self.contents = QWidget()
        self.contents_layout = QHBoxLayout(self.contents)
        self.contents_layout.setSpacing(80)
        # 위젯 배치
        self.contents_layout.addWidget(self.barcode_card)
        self.contents_layout.addWidget(self.manual_input_card)

        # 정중앙 배치를 위한 Stretch 조합
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(
            self.contents, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.main_layout.addStretch(1)




class BarcodePage(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._create_widget()
        self._create_layout()

        # 페이지가 열리면 바로 바코드 입력 가능
        self.barcode_input.setFocus()

    # --------------------------------------------------------
    # Widget
    # --------------------------------------------------------

    def _create_widget(self):

        # 안내 문구
        self.title_label = QLabel(
            "会員番号をスキャンしてください"
        )

        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 48px;
                font-weight: bold;
            }
        """)

        # 바코드 입력창
        self.barcode_input = QLineEdit()
        self.barcode_input.setFixedSize(1, 1)
        self.barcode_input.setStyleSheet("""
            QLineEdit {
                border: none;
                background: transparent;
                color: transparent;
                padding: 0px;
                margin: 0px;
            }
        """)

        # 바코드 스캐너가 Enter를 보내면 로그인
        self.barcode_input.returnPressed.connect(
            self._login
        )

    # --------------------------------------------------------
    # Layout
    # --------------------------------------------------------

    def _create_layout(self):

        layout = QVBoxLayout()

        layout.addStretch()

        layout.addWidget(
            self.title_label
        )

        layout.addSpacing(30)

        layout.addWidget(
            self.barcode_input
        )

        layout.addStretch()

        self.setLayout(layout)

    # --------------------------------------------------------
    # Login
    # --------------------------------------------------------

    def _login(self):
        # 입력된 바코드 번호
        member_no = self.barcode_input.text().strip()

        # 아무것도 입력하지 않았다면 무시
        if not member_no:
            self.barcode_input.setFocus()
            return

        data = {
            "type" : "login",
            "member_no" : member_no
        }

        print(member_no)
        
        respones = requests.get(
            BASE_URL,
            json=data
        )
        print("전송완료")
        self.barcode_input.setFocus()
      

    def _show_result_dialog(self, message):

        dialog = QDialog(self)

        # 터치 모니터에서 보기 편하도록 크게
        dialog.setMinimumSize(600, 350)

        layout = QVBoxLayout(dialog)

        # 메시지
        label = QLabel(message)

        label.setAlignment(Qt.AlignCenter)

        label.setWordWrap(True)

        label.setStyleSheet("""
            QLabel {
                font-size: 36px;
                font-weight: bold;
                padding: 30px;
            }
        """)

        # 확인 버튼
        ok_button = QPushButton("確認")

        # 터치하기 쉽게 크게
        ok_button.setMinimumHeight(90)

        ok_button.setStyleSheet("""
            QPushButton {
                font-size: 32px;
                font-weight: bold;
                border-radius: 15px;
                padding: 15px;
            }
        """)

        # 확인 버튼 → Dialog 종료
        ok_button.clicked.connect(
            dialog.accept
        )

        layout.addWidget(label)

        layout.addStretch()

        layout.addWidget(ok_button)

        # Dialog 실행
        dialog.exec()

        # ----------------------------------------------------
        # Dialog가 닫힌 후
        # ----------------------------------------------------

        # 기존 바코드 제거
        self.barcode_input.clear()

        # 다시 바코드 입력창으로 포커스
        self.barcode_input.setFocus()