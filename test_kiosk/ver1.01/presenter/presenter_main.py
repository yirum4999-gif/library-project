from presenter.cart_presenter import CartPresenter
from presenter.login_presenter import LoginPresenter
from utils.page_enum import Page
from utils.session import Session


class MainPresenter:
    """최상위 페이지 이동만 담당한다."""
    def __init__(self, view):
        self.view = view
        self.login_presenter = LoginPresenter(view.pages[Page.LOGIN])
        self.cart_presenter = CartPresenter(view.pages[Page.CART], self.show_home)
        home = view.pages[Page.HOME]
        home.loan_card.clicked.connect(self.start_loan)
        home.receive_card.clicked.connect(self.start_return)
        view.pages[Page.LOGIN].login_success.connect(self.open_loan_cart)
        self.show_home()

    def show_home(self):
        self.view.set_current_page(Page.HOME)

    def start_loan(self):
        Session.clear()
        self.login_presenter.show_scan()
        self.view.set_current_page(Page.LOGIN)

    def start_return(self):
        Session.clear()
        Session.transaction_mode = "return"
        self.cart_presenter.start("return")
        self.view.set_current_page(Page.CART)

    def open_loan_cart(self):
        Session.transaction_mode = "loan"
        self.cart_presenter.start("loan")
        self.view.set_current_page(Page.CART)
