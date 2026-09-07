import sys
import threading
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QStackedWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt, Signal, QObject

# ----------------------------------------------------
# 1. FastAPI Web Server & Signal Definition
# ----------------------------------------------------
class CommunicateSignal(QObject):
    # Java로부터 데이터 수신 시 UI를 안전하게 업데이트하기 위한 Signal
    received = Signal(str)

signal_helper = CommunicateSignal()
app = FastAPI()

# 수신할 JSON 데이터 구조 정의
class KioskMessage(BaseModel):
    sender: str
    message: str

@app.post("/api/receive")
async def receive_from_java(data: KioskMessage):
    formatted_msg = f"[{data.sender}] {data.message}"
    
    # Python 콘솔 출력
    print("==================================")
    print(f"[Python FastAPI Received] {formatted_msg}")
    print("==================================")
    
    # PySide6 UI 스레드로 데이터 전달
    signal_helper.received.emit(formatted_msg)
    return {"status": "SUCCESS", "message": "Message received by Python Kiosk"}

def start_fastapi():
    # 0.0.0.0으로 열어야 외부 Java 기기에서 IP로 접속 가능
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")


# ----------------------------------------------------
# 2. PySide6 GUI Application
# ----------------------------------------------------
class LibraryKiosk(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("図書館キオスク (受信対応)")
        self.resize(800, 600)

        # Signal 연결 (FastAPI 스레드 -> UI 스레드)
        signal_helper.received.connect(self.handle_received_message)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.init_main_page()
        self.init_auth_page()
        self.init_loan_page()

    def init_main_page(self):
        main_page = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("図書館セルフサービス")
        title_label.setStyleSheet("font-size: 32px; font-weight: bold; margin-bottom: 20px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 受信データ表示用ラベル (Java 수신 데이터 표시 라벨)
        self.recv_label = QLabel("Javaからの受信待機中...")
        self.recv_label.setStyleSheet("font-size: 16px; color: #555; background-color: #eee; padding: 10px; border-radius: 5px;")
        self.recv_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_layout = QHBoxLayout()

        self.btn_borrow = QPushButton("図書貸出")
        self.btn_borrow.setFixedSize(220, 140)
        self.btn_borrow.setStyleSheet("font-size: 22px; background-color: #4CAF50; color: white; border-radius: 10px;")
        self.btn_borrow.clicked.connect(self.go_to_auth_page)

        self.btn_return = QPushButton("図書返却")
        self.btn_return.setFixedSize(220, 140)
        self.btn_return.setStyleSheet("font-size: 22px; background-color: #2196F3; color: white; border-radius: 10px;")

        button_layout.addWidget(self.btn_borrow)
        button_layout.addSpacing(20)
        button_layout.addWidget(self.btn_return)

        layout.addWidget(title_label)
        layout.addWidget(self.recv_label)
        layout.addSpacing(20)
        layout.addLayout(button_layout)
        main_page.setLayout(layout)

        self.stacked_widget.addWidget(main_page)

    def init_auth_page(self):
        auth_page = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info_label = QLabel("会員証のバーコードをかざしてください")
        info_label.setStyleSheet("font-size: 26px; font-weight: bold; margin-bottom: 20px;")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.barcode_input = QLineEdit()
        self.barcode_input.setPlaceholderText("バーコード番号を入力またはスキャン")
        self.barcode_input.setFixedWidth(400)
        self.barcode_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.barcode_input.returnPressed.connect(self.verify_barcode)

        btn_verify = QPushButton("認証")
        btn_verify.setFixedWidth(400)
        btn_verify.setStyleSheet("font-size: 20px; padding: 10px; background-color: #FF9800; color: white;")
        btn_verify.clicked.connect(self.verify_barcode)

        btn_back = QPushButton("最初に戻る")
        btn_back.setFixedWidth(200)
        btn_back.setStyleSheet("font-size: 16px; margin-top: 30px;")
        btn_back.clicked.connect(self.go_to_main_page)

        layout.addWidget(info_label)
        layout.addWidget(self.barcode_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)
        layout.addWidget(btn_verify, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn_back, alignment=Qt.AlignmentFlag.AlignCenter)
        auth_page.setLayout(layout)

        self.stacked_widget.addWidget(auth_page)

    def init_loan_page(self):
        loan_page = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        success_label = QLabel("会員認証が完了しました。\n貸出する本をスキャンしてください。")
        success_label.setStyleSheet("font-size: 24px; color: #2E7D32;")
        success_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_home = QPushButton("最初に戻る")
        btn_home.setFixedWidth(200)
        btn_home.setStyleSheet("font-size: 16px; margin-top: 30px;")
        btn_home.clicked.connect(self.go_to_main_page)

        layout.addWidget(success_label)
        layout.addWidget(btn_home, alignment=Qt.AlignmentFlag.AlignCenter)
        loan_page.setLayout(layout)

        self.stacked_widget.addWidget(loan_page)

    def go_to_main_page(self):
        self.barcode_input.clear()
        self.stacked_widget.setCurrentIndex(0)

    def go_to_auth_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.barcode_input.setFocus()

    def verify_barcode(self):
        input_value = self.barcode_input.text().strip()
        if input_value == "MEMBER1234":
            self.stacked_widget.setCurrentIndex(2)
        else:
            QMessageBox.warning(self, "エラー", "有効な会員証ではありません。\nもう一度お試しください。")
            self.barcode_input.clear()
            self.barcode_input.setFocus()

    # Javaからメッセージを受信したときの処理 Slot
    def handle_received_message(self, text):
        self.recv_label.setText(f"受信メッセージ: {text}")


if __name__ == "__main__":
    # 백그라운드 스레드에서 FastAPI 실행
    fastapi_thread = threading.Thread(target=start_fastapi, daemon=True)
    fastapi_thread.start()

    app_qt = QApplication(sys.argv)
    kiosk = LibraryKiosk()
    kiosk.show()
    sys.exit(app_qt.exec())