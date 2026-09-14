<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library </title>
    <!-- 공통 CSS -->
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/resource/css/layout.css">
    <!-- 페이지 전용 CSS -->
    <% if (request.getAttribute("pageCss") != null) { %>
        <link rel="stylesheet"
              href="${pageContext.request.contextPath}/resource/css/${pageCss}">
    <% } %>
</head>
<body>
 	<header>
     	<ul>
         	<li><a href="index.do">Home</a></li>
         	<li><a href="login.do">로그인</a></li>
     	</ul>
    </header>
