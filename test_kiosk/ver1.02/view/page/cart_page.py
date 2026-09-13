from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHeaderView, QHBoxLayout, QLabel, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)

from view.components import BarcodeInput, ConfirmCancelCard


class CartPage(QWidget):
    """대출·반납 공용 카트. 표시/입력만 담당하고 요청은 CartPresenter가 맡는다."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_label = QLabel()
        self.available_label = QLabel()
        self.due_label = QLabel()
        self.scan_hint = QLabel("本のバーコードをスキャンしてください")
        self.book_input = BarcodeInput(self)
        self.cart_table = QTableWidget()
        self.action_card = ConfirmCancelCard("確定", "取消")
        self._create_layout()

    def _create_layout(self):
        for label in (self.user_label, self.available_label):
            label.setStyleSheet("font-size: 24px; font-weight: bold; color: #172554;")
        self.due_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.due_label.setStyleSheet("font-size: 25px; font-weight: bold; color: #B45309; padding: 14px; background: #FFFBEB; border-radius: 12px;")
        self.scan_hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scan_hint.setStyleSheet("font-size: 22px; color: #334155; padding: 8px;")
        self.cart_table.setAlternatingRowColors(True)
        self.cart_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.cart_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.cart_table.verticalHeader().setVisible(False)
        self.cart_table.horizontalHeader().setVisible(False)
        self.cart_table.setStyleSheet("QTableWidget { font-size: 20px; gridline-color: #CBD5E1; }")
        self.header_widget = QWidget()
        header = QHBoxLayout(self.header_widget)
        header.setContentsMargins(0, 0, 0, 0)
        header.addWidget(self.user_label)
        header.addStretch()
        header.addWidget(self.available_label)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(52, 36, 52, 36)
        layout.setSpacing(16)
        layout.addWidget(self.header_widget)
        layout.addWidget(self.due_label)
        layout.addWidget(self.scan_hint)
        layout.addWidget(self.book_input)
        layout.addWidget(self.cart_table, 1)
        layout.addWidget(self.action_card)

    def configure(self, mode, member_name, available_count):
        is_loan = mode == "loan"
        # 반납은 회원 인증 없이 가능하므로 회원 인사/대출 가능 권수 행을 표시하지 않는다.
        self.header_widget.setVisible(is_loan)
        self.user_label.setText(f"{member_name[:1]}×× 様、こんにちは")
        self.available_label.setText(f"現在 {available_count} 冊まで借りられます")
        self.due_label.setText("返却予定日：貸出日から 14 日" if is_loan else "最終延滞日：なし")
        self.cart_table.clearContents()
        self.cart_table.setRowCount(0)
        self.cart_table.setColumnCount(2)
        header = self.cart_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        self.cart_table.setColumnWidth(1, 240)
        self.book_input.setFocus()

    def add_book(self, book):
        row = self.cart_table.rowCount()
        self.cart_table.insertRow(row)
        for column, value in enumerate(book["row"]):
            item = QTableWidgetItem(str(value))
            if column == 1:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.cart_table.setItem(row, column, item)
        # 반납/연체 상태가 두 줄이므로 고정 행 높이로 문자 잘림을 막는다.
        self.cart_table.setRowHeight(row, 76)

    def set_overdue_date(self, date_text):
        self.due_label.setText(f"最終延滞日：{date_text or 'なし'}")
