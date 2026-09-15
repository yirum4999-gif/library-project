<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="model.*" %> 
<%@ page import="util.*" %>
<%@ page import="java.sql.* " %>
<%@ page import="java.time.LocalDateTime" %>
<%@ page import="java.sql.Timestamp" %>

<%

%>   

<%@ include file="/WEB-INF/views/includes/header.jsp" %>


<main class="container my-5">
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
			
			// 입력값 검증
		    if (!userId || !userPw) {
		        alert("아이디와 비밀번호를 모두 입력해주세요.");
		        return;
		    }
			
			const params = new URLSearchParams();
			params.append('userId', userId);
			params.append('userPw', userPw);
			
			fetch('${pageContext.request.contextPath}/login', {
		        method: 'POST',
		        headers: {
		            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
		        },
		        body: params
		    })
		    .then(response => {
		        if (!response.ok) {
		            throw new Error('network response was not ok');
		        }
		        return response.json(); // 서블릿에서 JSON 형태로 응답할 경우
		    })
		    .then(data => {
		        // 서블릿 응답 처리
		        if (data.success) {
		            alert('로그인 성공!');
		            location.href = '${pageContext.request.contextPath}/main'; // 성공 시 이동할 URL
		        } else {
		            alert(data.message || '로그인 실패: 아이디 또는 비밀번호를 확인하세요.');
		        }
		    })
		    .catch(error => {
		        console.error('Error:', error);
		        alert('로그인 처리 중 오류가 발생했습니다.');
		    });	
			
		}
	</script>

</main>

<%@ include file="/WEB-INF/views/includes/footer.jsp" %>

