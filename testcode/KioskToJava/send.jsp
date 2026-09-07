<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.io.OutputStream" %>
<%@ page import="java.net.HttpURLConnection" %>
<%@ page import="java.net.URL" %>
<%
    request.setCharacterEncoding("UTF-8");

    // 1. 질문자님(PySide6 실행 PC)의 192대 IP 주소를 입력해주세요.
    String pythonIp = "192.168.X.X"; // <-- 질문자님 IP로 수정
    String targetUrl = "http://" + pythonIp + ":8090/api/receive";

    String userText = request.getParameter("inputText");
    String statusMsg = "";

    // Form에서 텍스트를 입력하고 버튼을 눌렀을 때 실행
    if (userText != null && !userText.trim().isEmpty()) {
        try {
            URL url = new URL(targetUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
            conn.setDoOutput(true);
            conn.setConnectTimeout(3000);

            // 특수문자 및 따옴표 이스케이프 처리
            String safeText = userText.replace("\\", "\\\\").replace("\"", "\\\"");

            // JSON 데이터 생성
            String jsonInputString = "{\"sender\": \"Java_Web\", \"message\": \"" + safeText + "\"}";

            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int responseCode = conn.getResponseCode();
            if (responseCode == 200) {
                statusMsg = "<p style='color: green;'>送信成功: 「" + userText + "」</p>";
            } else {
                statusMsg = "<p style='color: red;'>送信失敗 (Response Code: " + responseCode + ")</p>";
            }

            conn.disconnect();
        } catch (Exception e) {
            statusMsg = "<p style='color: red;'>接続エラー: " + e.getMessage() + "</p>";
        }
    }
%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>PySide6 키오스크 전송 테스트</title>
    <style>
        body { font-family: sans-serif; padding: 30px; }
        .box { border: 1px solid #ccc; padding: 20px; border-radius: 8px; width: 400px; }
        input[type="text"] { width: 100%; padding: 10px; font-size: 16px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; margin-top: 10px; font-size: 16px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; }
    </style>
</head>
<body>

<div class="box">
    <h2>PySide6 키오스크로 데이터 전송</h2>
    
    <form method="post" action="send.jsp">
        <label for="inputText">보낼 메시지 입력:</label><br><br>
        <input type="text" id="inputText" name="inputText" placeholder="내용을 입력하세요..." required>
        <button type="submit">키오스크로 전송</button>
    </form>

    <div style="margin-top: 15px;">
        <%= statusMsg %>
    </div>
</div>

</body>
</html>