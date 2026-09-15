package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import util.DBManager;

public class LibraryMemberDAO {

    public int insertMember(LibraryMemberDTO dto) {

        // member_id 자리에 seq_member_id.NEXTVAL 적용 및 pin_password 컬럼 추가
        String sql = "INSERT INTO library_member (member_id, member_no, login_email, password_hash, pin_password, joined_at) "
                   + "VALUES (seq_member_id.NEXTVAL, ?, ?, ?, ?, SYSTIMESTAMP)";

        try (Connection conn = DBManager.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, dto.getMemberNo());
            pstmt.setString(2, dto.getLoginEmail());
            pstmt.setString(3, dto.getPasswordHash());
            pstmt.setInt(4, dto.getPinPassword()); // PIN 번호 바인딩

            return pstmt.executeUpdate();

        } catch (Exception e) {
            e.printStackTrace();
        }
        return 0;
    }

    public LibraryMemberDTO getMember(String loginEmail) {

        LibraryMemberDTO dto = null;

        String sql = "SELECT * FROM library_member WHERE login_email = ?";
        try (Connection conn = DBManager.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, loginEmail);

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    dto = new LibraryMemberDTO()
                            .setMemberId(rs.getInt("member_id"))
                            .setMemberNo(rs.getString("member_no"))
                            .setLoginEmail(rs.getString("login_email"))
                            .setPasswordHash(rs.getString("password_hash"))
                            .setPinPassword(rs.getInt("pin_password")) // PIN 번호 세팅
                            .setJoinedAt(rs.getTimestamp("joined_at"));

                    // penalty_end_date 처리 (Null 가능 컬럼)
                    if (rs.getTimestamp("penalty_end_date") != null) {
                        dto.setPenaltyEndDate(rs.getTimestamp("penalty_end_date").toLocalDateTime());
                    }

                    return dto;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return dto;
    }
}
