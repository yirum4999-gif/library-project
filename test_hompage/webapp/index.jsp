<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="model.*" %> 
<%@ page import="utils.*" %>
<%@ page import="java.sql.* " %>
<%@ page import="java.time.LocalDateTime" %>
<%@ page import="java.sql.Timestamp" %>

<%
	
%>   

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>

<body>
	<h2>MVC 패턴 비동기 로그인</h2>
    <form id="loginForm">
        <div class="form-group">
            <label for="userId">아이디:</label>
            <input type="text" id="userId" name="userId">
        </div>
        <div class="form-group">
            <label for="userPw">비밀번호:</label>
            <input type="password" id="userPw" name="userPw">
        </div>
        <button type="button" onclick="handleLogin()">로그인</button>
    </form>
    <script>
    
		function handleLogin() {
			const userId = document.getElementById('userId').value;
			const userPw = document.getElementById('userPw').value;
			
			const params = new URLSearchParams();
			params.append('userId', userId);
			params.append('userPw', userPw);
				
			
		}
	</script>
</body>

</html>