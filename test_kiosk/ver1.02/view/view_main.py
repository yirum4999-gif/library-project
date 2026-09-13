# view_main.py

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from utils.page_enum import Page

class UiCofing():
    def __init__(self):
        pass

    def set_screen_ratio(self,widget, w_ratio :float,h_ratio :float = None):
        """
        모니터 해상도에 맞게 크기를 변경하는 메서드
        """
        if h_ratio is None:
            h_ratio = w_ratio

        screen = QApplication.primaryScreen().geometry()

        # 모니터 크기를 가져와 비율에 맞게 프로그램 윈도우 크기 설정
        width = int(screen.width() * w_ratio)
        height = int(screen.height() * h_ratio)

        """
        정중앙에 배치하기 위해 값을 나누기
        화면을 차지한 남는 값을 2로 나누면 여백이 균등하게 들어감 
        EX: y = (1200-800) /2 => 400/2 =>  위아래 여백으로 200씩 가져감
        """
        x =  int((screen.width() - width) / 2) 
        y =  int((screen.height() - height) / 2)

        widget.setGeometry(x, y, width, height)

         
class MainWindowViewToStacked(QMainWindow):
    def __init__(self,uiconfig : UiCofing, pages: dict):
        super().__init__()

        self.uiconfig = uiconfig
        # 전체 화면을 해제했을 때 되돌아갈 기본 창 크기(70%)를 보존한다.
        self.uiconfig.set_screen_ratio(self, 0.7)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.pages = pages          # 페이지 객체 보관
        self.page_index = {}        # Enum → 인덱스

        self.init_stacked_pages()

    def init_stacked_pages(self):
        """
        enumerate를 사용하여 회숫의 값을 인덱스로 받아오며 키와 밸류를 튜플로 받습니다.
        순서대로 stacked_widget에 페이지를 추가하고, enum의 이름을 갖는 딕셔너리가 인덱스를 갖도록 합니다.
        따라서 실행하는 enum값은 달라져도 실제 enum의 값은 변경되지 않습니다.
        """
        for index, (page_enum, page) in enumerate(self.pages.items()):
            self.stacked_widget.addWidget(page)
            self.page_index[page_enum] = index
    
 
    def set_current_page(self, page: Page):
       """ 
       presenter 에게 변경 위젯을 위임할 set클래스 
       presenter가 위젯 순서를 정합니다.
       """
       self.stacked_widget.setCurrentIndex(self.page_index[page])

    def leave_full_screen(self):
        """Esc/F11로 전체 화면을 끝내면 초기 70% 중앙 창으로 복귀한다."""
        self.showNormal()
        self.uiconfig.set_screen_ratio(self, 0.7)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Escape, Qt.Key.Key_F11):
            if self.isFullScreen():
                self.leave_full_screen()
                event.accept()
                return
            if event.key() == Qt.Key.Key_F11:
                self.showFullScreen()
                event.accept()
                return
        super().keyPressEvent(event)

