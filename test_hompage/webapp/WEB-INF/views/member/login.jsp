<%@ page language="java" contentType="text/html; charset=UTF-8"

pageEncoding="UTF-8"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>

<html lang="ja">

<head>

<meta charset="utf-8">

<meta name="keywords" content="Library name">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Library login</title>

<!-- bootstrap + bootstrap icon -->

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

<!-- css -->

<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/common.css">

<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/layout.css">

<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/custom.css">

</head>

<body class="login-page d-flex flex-column min-vh-100">

<!-- Top notice (Announce) -->

<div class="top_notice">

<div class="top_notice_inner d-flex justify-content-between align-items-center py-2">

<div class="d-flex align-items-center gap-2 flex-grow-1">

<span class="notice_badge">Notice!</span>

<a href="#" class="notice_link">Please write the notice here</a>

</div>

<div class="d-none d-md-flex align-items-center gap-3 flex-shrink-0 me-1">

<span class="notice_hours"><i class="bi bi-clock me-1"></i>Open Today : <strong>9:00 AM - 06:00 PM</strong></span>

<span class="notice_status"><i class="bi bi-check-circle-fill me-1"></i>Open as usual</span>

</div>

<!-- language switcher -->

<div class="language_switcher dropdown ms-3">

<button class="btn btn-sm btn-outline-light dropdown-toggle" type="button"

id="languageDropdown" data-bs-toggle="dropdown" aria-expanded="false">

<i class="bi bi-globe2 me-1"></i> 🇯🇵 日本語

</button>

<ul class="dropdown-menu dropdown-menu-end" aria-labelledby="languageDropdown">

<li><a class="dropdown-item active" href="#">🇯🇵 日本語</a></li>

<li><a class="dropdown-item" href="#">🇰🇷 한국어</a></li>

</ul>

</div>

</div>

</div>

  

<!-- main header & navigation -->

<header class="sticky-top" style="background-color: #fff;">

<div class="header_main">

<div class="container-xxl px-3 px-sm-4 px-lg-5">

<div class="d-flex justify-content-between align-items-center" style="height: 5rem;">

<!-- logo -->

<div class="logo d-flex align-items-center gap-2" style="cursor: pointer;" onclick="location.href='${pageContext.request.contextPath}/main.do'">

<div class="logo_icon">

<img src="${pageContext.request.contextPath}/asset-img/Emb_Chiba.svg" alt="logo" class="logo_img">

</div>

<div class="logo_text d-flex flex-column">

<span class="fs-4 fw-bold text-dark">モックアップ<span style="color: var(--brand-primary); margin-left: 5px;">ページ</span></span>

<p class="text-md-start fw-normal text-dark" style="letter-spacing: 2px;"> mock up page </p>

</div>

</div>

<!-- Desktop Nav Navigation Links -->

<nav class="d-none d-lg-flex align-items-center gap-4 text-secondary fw-semibold fs-6">

<a class="gnb-link" href="${pageContext.request.contextPath}/searchBook/search.do">統合検索</a>

<a class="gnb-link" href="#">利用案内</a>

<a class="gnb-link" href="#">希望図書・相互貸借</a>

<a class="gnb-link" href="#">電子図書館</a>

<a class="gnb-link d-flex align-items-center gap-1 fw-bold" href="${pageContext.request.contextPath}/mypage.do">

<i class="bi bi-person-fill"></i>マイページ

</a>

</nav>

  

<!-- User Quick Info / Mobile Toggle -->

<div class="header-actions">

<c:choose>

<c:when test="${empty sessionScope.loginUser}">

<div class="login-btn d-none d-sm-flex align-items-center gap-2 p-2 small" role="button" onclick="location.href='${pageContext.request.contextPath}/member/login.do'">

<span><strong id="login-btn" class="fw-bold fs-5">ログイン</strong></span>

</div>

</c:when>

<c:otherwise>

<div class="user_info d-none d-sm-flex align-items-center gap-2 bg-light p-2 rounded border border-secondary-subtle small">

<span class="rounded-circle bg-success status-dot-pulse"></span>

<span><strong id="userName" class="me-1">${sessionScope.loginUser.userName}</strong>様</span>

</div>

</c:otherwise>

</c:choose>

</div>

</div>

</div>

</div>

</header>

  

<!-- 페이지 안내 히어로 -->

<div class="page-hero align-items-center text-white w-100 px-5 py-2">

<h1 class="fw-bold mb-0"> ログイン </h1>

</div>

  

<main class="subpage-main d-flex flex-column flex-grow-1 align-items-center p-3">

<div class="login-box">

<div class="login-content">

<div class="login-header d-flex align-items-center mb-4">

<i class="bi bi-person-lock fs-4 me-2"></i>

<h2 class="h4 fw-bold mb-0">ログイン</h2>

</div>

  

<!-- 로그인 에러 메시지 출력 예시 -->

<c:if test="${not empty errorMessage}">

<div class="alert alert-danger py-2 small mb-3" role="alert">

${errorMessage}

</div>

</c:if>

  

<!-- Login Form (서블릿 전송 처리) -->

<form id="loginForm" action="${pageContext.request.contextPath}/member/login.do" method="post">

<div class="login-form-row d-flex align-items-center">

<div class="login-fields">

<!-- ID -->

<div class="row align-items-center mb-3">

<label for="loginId" class="col-12 col-sm-3 col-form-label fw-semibold">

アイディー

</label>

<div class="col-12 col-sm-9">

<input type="text" id="loginId" name="loginId" class="form-control" autocomplete="username" required>

</div>

</div>

  

<!-- Password -->

<div class="row align-items-center">

<label for="loginPassword" class="col-12 col-sm-3 col-form-label fw-semibold">

パスワード

</label>

<div class="col-12 col-sm-9">

<input type="password" id="loginPassword" name="loginPassword" class="form-control" autocomplete="current-password" required>

</div>

</div>

</div>

  

<!-- Login Button -->

<button type="submit" class="btn btn-sm login-submit-btn text-white" style="background-color: var(--brand-primary);">

<i class="bi bi-box-arrow-in-right fs-4 mb-0"></i>

<span>ログイン</span>

</button>

</div>

</form>

  

<!-- Links (회원가입, 아이디/비밀번호 찾기 연결) -->

<div class="border-top mt-4 pt-3 d-flex justify-content-center align-items-center gap-3">

<!-- 이 코드는 회원가입이랑 email 인증 테스트 하려고 임시로 제가 갈겨놓은 코드입니다. -->

<%-- <a href="${pageContext.request.contextPath}/register.jsp" class="login-link">

会員登録

</a> --%>

<!-- 인증번호 가는거 테스트해보려고 잠깐 바로 register.jsp 로 이동하게끔 수정해 놨습니다.

실제로는 밑에처럼 join.do 로 해야 되는게 맞아요 -->

<a href="${pageContext.request.contextPath}/member/join.do" class="login-link">

会員登録

</a>

<span class="login-link-divider">|</span>

<a href="${pageContext.request.contextPath}/member/findAccount.do" class="login-link">

アイディー・パスワードを探す

</a>

</div>

</div>

</div>

</main>

  

<!-- Footer -->

<footer class="bg-dark text-secondary small py-5 border-top border-secondary">

<div class="container-lg px-4">

<div class="d-flex flex-column flex-md-row justify-content-between align-items-start align-items-md-center gap-3 border-bottom border-secondary pb-4 mb-4">

<div class="d-flex align-items-center gap-1 text-white fw-bold fs-5">

<img class="footer_img" src="${pageContext.request.contextPath}/asset-img/gov_gosann-kiri.svg" alt="gosann-kiri">

<i class="fw-semibold"></i> Library mock up page

</div>

<div class="footer-util d-flex flex-wrap gap-4 fw-medium">

<a href="#" class="nav-link p-0 text-secondary">プライバシーポリシー</a>

<a href="#" class="nav-link p-0 text-secondary">利用規約</a>

<a href="#" class="nav-link p-0 text-secondary">図書館の自由に関する宣言</a>

<a href="#" class="nav-link p-0 text-secondary">アクセス</a>

</div>

</div>

<div class="d-flex flex-column flex-sm-row justify-content-between text-secondary gap-2">

<p class="mb-0"> 〒000-0000 Need Japanese address | TEL: 043-1234-5678 | FAX: 043-1234-5679</p>

<p class="mb-0"> © 2026 Library mock up page. For testing purposes only. No distribution or modification permitted.</p>

</div>

</div>

</footer>

  

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>

<script src="${pageContext.request.contextPath}/script/main.js"></script>

</body>

</html>