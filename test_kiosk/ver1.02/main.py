# main.py

import sys
from PySide6.QtWidgets import QApplication
from view.view_main import UiCofing, MainWindowViewToStacked
from presenter.presenter_main import MainPresenter
from view.page.home_page import HomePage
from view.page.login_page import LoginPage
from view.page.cart_page import CartPage
from utils.page_enum import Page

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # UI 설정 및 페이지 준비
    ui_config = UiCofing()

    #page 인스턴스 생성
    home_page = HomePage()
    login_page= LoginPage()
    cart_page = CartPage()


    pages = {
        Page.HOME: home_page,
        Page.LOGIN: login_page,
        Page.CART:   cart_page
    }

    # View 및 Presenter 생성
    main_view = MainWindowViewToStacked(uiconfig=ui_config, pages=pages)
    presenter = MainPresenter(view=main_view)

    # 화면 표시 및 앱 실행
    # 전체 화면에서는 운영체제의 제목 표시줄/닫기 버튼이 보이지 않는다.
    # Esc 또는 F11을 누르면 view_main의 70% 중앙 창 크기로 되돌아간다.
    main_view.showFullScreen()

    sys.exit(app.exec())
