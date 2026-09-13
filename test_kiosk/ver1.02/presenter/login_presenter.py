import requests
from utils.session import Session
from view.components import InfoDialog

BASE_URL = "http://localhost:8000/api/kiosk"


class LoginPresenter:
    """로그인 내부의 스캔 → 수기입력 → PIN 흐름만 담당한다."""
    def __init__(self, view):
        self.view, self.login_token = view, None
        view.scan_page.barcode_input.barcodeEntered.connect(self.request_member)
        view.scan_page.manual_input_card.clicked.connect(self.show_manual)
        view.manual_page.member_submitted.connect(self.request_member)
        view.manual_page.action_card.cancelled.connect(self.show_scan)
        view.pin_page.pin_submitted.connect(self.verify_pin)
        view.pin_page.action_card.cancelled.connect(self.show_scan)

    def show_scan(self):
        self.view.stack.setCurrentWidget(self.view.scan_page)
        self.view.scan_page.barcode_input.setFocus()

    def show_manual(self):
        self.view.manual_page.member_input.clear()
        self.view.stack.setCurrentWidget(self.view.manual_page)
        self.view.manual_page.member_input.setFocus()

    def request_member(self, member_no):
        if not member_no:
            InfoDialog("入力エラー", "会員番号を入力してください。", self.view).exec()
            return
        result = self._post({
            "type": "login", 
            "member_no": member_no
        })
        if result and result.get("success"):
            self.login_token = result.get("login_token")
            Session.member_no = member_no
            Session.member_name = result.get("member_name", "利用者")
            Session.available_count = result.get("available_count", 0)
            self.view.pin_page.clear()
            self.view.stack.setCurrentWidget(self.view.pin_page)
        elif result:
            InfoDialog("認証できません", result.get("message", "会員番号を確認してください。"), self.view).exec()

    def verify_pin(self, pin):
        if not pin:
            InfoDialog("入力エラー", "暗証番号を入力してください。", self.view).exec()
            return
        result = self._post({"type": "verify_pin", "member_no": Session.member_no,
                             "login_token": self.login_token, "pin": pin})
        if result and result.get("success"):
            Session.is_login = True
            self.view.login_success.emit()
        elif result:
            InfoDialog("認証できません", result.get("message", "暗証番号を確認してください。"), self.view).exec()
            self.view.pin_page.clear()

    def _post(self, payload):
        try:
            response = requests.post(BASE_URL, json=payload, timeout=8)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError):
            InfoDialog("通信エラー", "サーバーに接続できません。係員にお知らせください。", self.view).exec()
            return None
