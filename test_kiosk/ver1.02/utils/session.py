class Session:
    # 로그인 여부 
    is_login = False 
    # 로그인한 회원 번호
    member_no = None
    #빌릴 수 있는 책 수
    available_count = 0
    transaction_mode = None  # "loan" 또는 "return"
    member_name = None

    @classmethod
    def clear(cls):
        cls.is_login = False
        cls.member_no = None
        cls.member_name = None
        cls.available_count = 0
        cls.transaction_mode = None
