package model;

//=======================================
//이름 : LibraryMemberDTO.java
//이 코드의 역할 : library_member 테이블의 데이터를 담는 DTO(Data Transfer Object) 클래스
//setter 메서드들은 메서드 체이닝을 지원하도록 수정(09/14)
//PIN 번호(pin_password) 필드 추가 (09/15)
//=======================================
import java.sql.Timestamp;
import java.time.LocalDateTime;

public class LibraryMemberDTO {

    private int memberId;
    private String memberNomber;
    private String loginEmail;
    private String passwordHash;
    private LocalDateTime penaltyEndDate;
    private Timestamp joinedAt;
    private int pinPassword; // PIN 번호 추가 (NUMBER 타입에 대응)

    public LibraryMemberDTO() {
        // 기본 생성자
    }
    
    public int getMemberId() {
        return memberId;
    }

    public LibraryMemberDTO setMemberId(int memberId) {
        this.memberId = memberId;
        return this;
    }

    public String getMemberNo() {
        return memberNomber;
    }

    public LibraryMemberDTO setMemberNo(String memberNo) {
        this.memberNomber = memberNo;
        return this;
    }

    public String getLoginEmail() {
        return loginEmail;
    }

    public LibraryMemberDTO setLoginEmail(String loginEmail) {
        this.loginEmail = loginEmail;
        return this;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public LibraryMemberDTO setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
        return this;
    }

    public LocalDateTime getPenaltyEndDate() {
        return penaltyEndDate;
    }

    public LibraryMemberDTO setPenaltyEndDate(LocalDateTime penaltyEndDate) {
        this.penaltyEndDate = penaltyEndDate;
        return this;
    }

    public Timestamp getJoinedAt() {
        return joinedAt;
    }

    public LibraryMemberDTO setJoinedAt(Timestamp joinedAt) {
        this.joinedAt = joinedAt;
        return this;
    }

    public int getPinPassword() {
        return pinPassword;
    }

    public LibraryMemberDTO setPinPassword(int pinPassword) {
        this.pinPassword = pinPassword;
        return this;
    }
}
