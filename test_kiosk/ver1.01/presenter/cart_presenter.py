import requests
from utils.session import Session
from view.components import ConfirmDialog, InfoDialog

BASE_URL = "http://localhost:8000/api/kiosk"


class CartPresenter:
    """공용 카트의 도서 스캔과 원자적 확정 요청을 담당한다."""
    def __init__(self, view, go_home):
        self.view, self.go_home, self.mode, self.barcodes = view, go_home, None, []
        view.book_input.barcodeEntered.connect(self.scan_book)
        view.action_card.confirmed.connect(self.confirm)
        view.action_card.cancelled.connect(self.cancel)

    def start(self, mode):
        self.mode, self.barcodes = mode, []
        name = Session.member_name if mode == "loan" else "返却のお客様"
        self.view.configure(mode, name, Session.available_count if mode == "loan" else 0)

    def scan_book(self, barcode):
        result = self._post({"type": "scan_book", "mode": self.mode,
                             "member_no": Session.member_no, "book_barcode": barcode})
        if not result:
            return
        if not result.get("success"):
            InfoDialog("登録できません", result.get("message", "この本は処理できません。"), self.view).exec()
            return
        if barcode in self.barcodes:
            InfoDialog("重複スキャン", "この本はすでにカートにあります。", self.view).exec()
            return
        book = result.get("book", {})
        if self.mode == "loan":
            row = (book.get("title", "不明な書名"), book.get("loanable", "可"))
        else:
            row = (book.get("title", "不明な書名"), book.get("returnable", "可"), book.get("overdue", "なし"))
            self.view.set_overdue_date(result.get("max_overdue_date"))
        self.barcodes.append(barcode)
        self.view.add_book({"row": row})

    def confirm(self):
        if not self.barcodes:
            InfoDialog("カートが空です", "本のバーコードをスキャンしてください。", self.view).exec()
            return
        verb = "貸出" if self.mode == "loan" else "返却"
        if ConfirmDialog("処理の確認", f"{len(self.barcodes)} 冊を{verb}しますか？", self.view).exec() != ConfirmDialog.DialogCode.Accepted:
            return
        result = self._post({"type": "process_transaction", "mode": self.mode,
                             "member_no": Session.member_no, "book_barcodes": self.barcodes})
        if result and result.get("success"):
            InfoDialog("処理完了", result.get("message", f"{verb}処理が完了しました。"), self.view).exec()
            self.cancel()
        elif result:
            InfoDialog("処理できません", result.get("message", "処理は取り消されました。"), self.view).exec()

    def cancel(self):
        Session.clear()
        self.barcodes.clear()
        self.go_home()

    def _post(self, payload):
        try:
            response = requests.post(BASE_URL, json=payload, timeout=8)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError):
            InfoDialog("通信エラー", "サーバーに接続できません。係員にお知らせください。", self.view).exec()
            return None
