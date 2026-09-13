from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

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
        self.cart_table.setStyleSheet("QTableWidget { font-size: 20px; gridline-color: #CBD5E1; } QHeaderView::section { font-size: 20px; font-weight: bold; padding: 12px; background: #E0E7FF; }")
        header = QHBoxLayout()
        header.addWidget(self.user_label)
        header.addStretch()
        header.addWidget(self.available_label)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(52, 36, 52, 36)
        layout.setSpacing(16)
        layout.addLayout(header)
        layout.addWidget(self.due_label)
        layout.addWidget(self.scan_hint)
        layout.addWidget(self.book_input)
        layout.addWidget(self.cart_table, 1)
        layout.addWidget(self.action_card)

    def configure(self, mode, member_name, available_count):
        is_loan = mode == "loan"
        self.user_label.setText(f"{member_name[:1]}×× 様、こんにちは")
        self.available_label.setText(f"現在 {available_count} 冊まで借りられます")
        self.due_label.setText("返却予定日：貸出日から 14 日" if is_loan else "最終延滞日：なし")
        headers = ("書名", "貸出可否") if is_loan else ("書名", "返却", "延滞")
        self.cart_table.clearContents()
        self.cart_table.setRowCount(0)
        self.cart_table.setColumnCount(len(headers))
        self.cart_table.setHorizontalHeaderLabels(headers)
        self.cart_table.horizontalHeader().setStretchLastSection(True)
        self.book_input.setFocus()

    def add_book(self, book):
        row = self.cart_table.rowCount()
        self.cart_table.insertRow(row)
        for column, value in enumerate(book["row"]):
            self.cart_table.setItem(row, column, QTableWidgetItem(str(value)))
        self.cart_table.resizeColumnsToContents()

    def set_overdue_date(self, date_text):
        self.due_label.setText(f"最終延滞日：{date_text or 'なし'}")
