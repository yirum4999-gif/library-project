package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import util.DBManager;

public class LibraryMemberDAO {

	
	public int insertMember(LibraryMemberDTO dto) {

	    // member_id 자리에 seq_member_id.NEXTVAL 적용
	    String sql = "INSERT INTO library_member (member_id, member_no, login_email, password_hash, joined_at) "
	               + "VALUES (seq_member_id.NEXTVAL, ?, ?, ?, SYSTIMESTAMP)";

	    try(Connection conn = DBManager.getConnection();
	        PreparedStatement pstmt = conn.prepareStatement(sql)) {
	  

	        // member_no는 고유한 값이어야 하므로 전달받은 값을 넣거나, 테스트 시 임의 문자열 세팅 필요
	        pstmt.setString(1, dto.getMemberNo());
	        pstmt.setString(2, dto.getLoginEmail());
	        pstmt.setString(3, dto.getPasswordHash());

	        return pstmt.executeUpdate();

	    } catch (Exception e) {
	        e.printStackTrace();
	    }
	    return 0;
	}
	
	public LibraryMemberDTO getMember(String loginEmail) {
		
		LibraryMemberDTO dto = null;

		String sql = "select * from library_member where login_email = ?";
		try(Connection conn = DBManager.getConnection();
			PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setString(1, loginEmail);
			
			try(ResultSet rs = pstmt.executeQuery()) {
				if (rs.next()) {
					dto = new LibraryMemberDTO().setMemberId(rs.getInt("member_id"))
					.setMemberNo(rs.getString("member_no"))
					.setLoginEmail(rs.getString("login_email"))
					.setPasswordHash(rs.getString("password_hash"));
					
			        return dto;	
				}
				
			}
		 } catch (Exception e) {
			        e.printStackTrace();
			    }
		
		return dto;
	}
	
	
}
