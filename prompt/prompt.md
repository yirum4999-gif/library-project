# 도서관 테이블


```sql

--도서관 회원--

--시퀀스--
CREATE SEQUENCE seq_member_id
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

--생성--
CREATE TABLE library_member (
    member_id          NUMBER              NOT NULL,
    member_no          VARCHAR2(30 CHAR)   NOT NULL,
    login_email        VARCHAR2(254 CHAR)  NOT NULL,
    password_hash      VARCHAR2(255 CHAR)  NOT NULL,
    pin_password       NUMBER              NOT NULL,
    penalty_end_date   DATE                NULL,
    joined_at          TIMESTAMP DEFAULT SYSTIMESTAMP NOT NULL,

    CONSTRAINT pk_library_member PRIMARY KEY (member_id),
    CONSTRAINT uk_library_member_email UNIQUE (login_email),
    CONSTRAINT uk_library_member_no UNIQUE (member_no)
);
```
