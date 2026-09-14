<%@ page language="java" contentType="text/html; charset=UTF-8"

pageEncoding="UTF-8"%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>

<html lang="ja">

<head>

<meta charset="utf-8">

<meta name="keywords" content="Library name">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Library register</title>

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

<li><a class="dropdown-item active" href="/ja/">🇯🇵 日本語</a></li>

<li><a class="dropdown-item" href="/ko/">🇰🇷 한국어</a></li>

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

<div class="logo d-flex align-items-center gap-2" style="cursor: pointer;" onclick="switchNav('main')">

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

<a class="gnb-link" onclick="switchNav('search')">統合検索</a>

<a class="gnb-link" onclick="switchNav('info')">利用案内</a>

<a class="gnb-link" onclick="switchNav('request')">希望図書・相互貸借</a>

<a class="gnb-link" onclick="switchNav('data-library')">電子図書館</a>

<a class="gnb-link d-flex align-items-center gap-1 fw-bold" onclick="switchNav('mypage')">

<i class="bi bi-person-fill"></i>マイページ

</a>

</nav>

<!-- User Quick Info / Mobile Toggle -->

<div class="header-actions">

<div class="login-btn d-none d-sm-flex align-items-center gap-2 p-2 small" role="button">

<span><strong id="login-btn" class="fw-bold fs-5">ログイン</strong></span>

</div>

<button type="button"

onclick="location.href = '#'"

class="d-lg-none btn btn-light text-secondary border rounded p-0 d-flex align-items-center justify-content-center"

style="width: 42px; height: 42px;">

<i class="bi bi-person-fill-exclamation d-inline-flex fs-5"></i>

</button>

</div>

</div>

</div>

</div>

  

<!-- Mobile Access: Submenu -->

<div class="bg-light border-top px-2 py-2 d-lg-none d-flex justify-content-around text-secondary small overflow-auto text-nowrap">

<a class="gnb-link px-sm-1 fw-semibold" onclick="switchNav('search')">統合検索</a>

<a class="gnb-link px-sm-1 fw-semibold" onclick="switchNav('info')">利用案内</a>

<a class="gnb-link px-sm-1 fw-semibold" onclick="switchNav('request')">希望図書</a>

<a class="gnb-link px-sm-1 fw-semibold" onclick="switchNav('data-library')">電子図書館</a>

<a class="gnb-link px-sm-1 fw-bold" onclick="switchNav('mypage')">マイページ</a>

</div>

</header>

  

<!-- 페이지 안내 히어로 -->

<div class="page-hero align-items-center text-white w-100 px-5 py-2">

<h1 class="fw-bold mb-0"> 会員登録 </h1>

</div>

  

<main class="subpage-main d-flex flex-column flex-grow-1 align-items-center p-3">

<div class="register-area border border-secondary-subtle rounded-3 py-4 py-md-5">

<div class="register-header d-flex align-items-center mb-4">

<i class="bi bi-person-plus fs-4 me-2"></i>

<h2 class="h4 fw-bold mb-0">会員登録</h2>

</div>

  

<!-- MemberController 매핑 경로(/member/join.do)로 수정 완료 -->

<form id="registerForm" action="${pageContext.request.contextPath}/member/join.do" method="post">

<div class="table-responsive">

<table class="table register-table align-middle mb-0">

<tbody>

<!-- ID -->

<tr>

<th scope="row">

<label for="registerId">アイディー</label>

</th>

<td>

<div class="register-input-row d-flex align-items-center gap-2">

<input type="text" id="registerId" name="registerId" class="form-control" autocomplete="username" required>

<button type="button"

id="checkIdBtn"

class="btn flex-shrink-0 text-nowrap text-white"

style="background-color: var(--brand-primary);">

<i class="bi bi-person-check-fill"></i>

<span>重複チェック</span>

</button>

</div>

<div id="idCheckMessage" class="form-text mt-1"></div>

</td>

</tr>

  

<!-- Password -->

<tr>

<th scope="row">

<label for="registerPassword">パスワード</label>

</th>

<td>

<input type="password" id="registerPassword" name="registerPassword" class="form-control register-input" autocomplete="new-password" required>

</td>

</tr>

  

<!-- Password Confirm -->

<tr>

<th scope="row">

<label for="registerPasswordConfirm">

パスワード（確認）

</label>

</th>

<td>

<input type="password" id="registerPasswordConfirm" name="registerPasswordConfirm" class="form-control register-input" autocomplete="new-password" required>

</td>

</tr>

  

<!-- Email -->

<tr>

<th scope="row">

<label for="registerEmail">メールアドレス</label>

</th>

<td>

<div class="email-input register-input-row">

<input type="email" id="registerEmail" name="registerEmail" class="form-control register-input" placeholder="example@gmail.com" autocomplete="email" required>

  

<button type="button" id="sendEmailCodeBtn"

class="btn flex-shrink-0 text-nowrap text-white"

style="background-color: var(--brand-primary);">

<i class="bi bi-envelope-check"></i>

<span class="d-none d-md-inline">メール認証</span>

</button>

</div>

  

<!-- 인증번호 -->

<div id="emailVerificationWrap" class="d-flex justify-content-start align-items-center gap-2 mt-2">

<div>

<input type="text" id="emailVerificationCode" class="form-control text-center" placeholder="認証番号 6字">

</div>

<button type="button" id="verifyEmailCodeBtn" class="btn btn-outline-success flex-shrink-0">確認</button>

</div>

  

<!-- 인증 상태 -->

<div id="emailVerificationMessage" class="form-text mt-1">

</div>

</td>

</tr>

</tbody>

</table>

</div>

  

<!-- Buttons -->

<div class="register-actions d-flex justify-content-center gap-3 mt-4">

<button type="reset" class="btn btn-outline-secondary px-4">

リセット

</button>

  

<button type="submit" class="btn text-white px-4" style="background-color: var(--brand-primary);">

<i class="bi bi-person-plus me-1"></i>

会員登録

</button>

</div>

</form>

</div>

</main>

  

<!-- Footer -->

<footer class="bg-dark text-secondary small py-5 mt-5 border-top border-secondary">

<div class="container-lg px-4">

<div class="d-flex flex-column flex-md-row justify-content-between align-items-start align-items-md-center gap-3 border-bottom border-secondary pb-4 mb-4">

<div class="d-flex align-items-center gap-1 text-white fw-bold fs-5">

<img class="footer_img" src="${pageContext.request.contextPath}/asset-img/gov_gosann-kiri.svg" alt="gosann-kiri">

<i class="fw-semibold"></i> Library mock up page

</div>

<div class="footer-util d-flex flex-wrap gap-4 fw-medium flex-nowrap">

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

  

<!-- J Query -->

<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>

<!-- Boot Strap Java Script-->

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>

<script src="${pageContext.request.contextPath}/script/calendar.js"></script>

<script src="${pageContext.request.contextPath}/script/main.js"></script>

  

<script>

$(function () {

window.idChecked = false;

window.emailVerified = false;

  

/* ID 실시간 검증 */

$('#registerId').on('input', function () {

const id = $.trim($(this).val());

window.idChecked = false;

$('#idCheckMessage').text('').removeClass('text-success text-danger');

  

if (!id) return;

if (!/^[a-zA-Z0-9]{4,20}$/.test(id)) {

$('#idCheckMessage').text('アイディーは4~20文字の英数字で入力してください。')

.removeClass('text-success').addClass('text-danger');

}

});

  

/* Password 실시간 검증 */

$('#registerPassword').on('input', function () {

const password = $(this).val();

if (!password) {

$(this).removeClass('is-valid is-invalid');

return;

}

if (password.length < 8) {

$(this).removeClass('is-valid').addClass('is-invalid');

} else {

$(this).removeClass('is-invalid').addClass('is-valid');

}

});

  

/* Password Confirm 실시간 검증 */

$('#registerPasswordConfirm').on('input', function () {

const password = $('#registerPassword').val();

const confirmPassword = $(this).val();

if (!confirmPassword) {

$(this).removeClass('is-valid is-invalid');

return;

}

if (password !== confirmPassword) {

$(this).removeClass('is-valid').addClass('is-invalid');

} else {

$(this).removeClass('is-invalid').addClass('is-valid');

}

});

  

/* Email 실시간 검증 */

$('#registerEmail').on('input', function () {

const email = $.trim($(this).val());

if (!email) {

$(this).removeClass('is-valid is-invalid');

return;

}

if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {

$(this).removeClass('is-valid').addClass('is-invalid');

} else {

$(this).removeClass('is-invalid').addClass('is-valid');

}

});

  

/* ID 중복 체크 (테스트용) */

$('#checkIdBtn').on('click', function () {

const id = $.trim($('#registerId').val());

if (!id) return;

  

$('#checkIdBtn').prop('disabled', true).text('確認中...');

setTimeout(function () {

window.idChecked = true;

$('#checkIdBtn').prop('disabled', false).text('確認済み');

$('#idCheckMessage').text('使用可能なアイディーです。')

.removeClass('text-danger').addClass('text-success');

}, 500);

});

  

/* 1. 인증메일 전송 AJAX (SendEmailController 연동) */

$('#sendEmailCodeBtn').on('click', function () {

const email = $.trim($('#registerEmail').val());

  

if (!email) {

alert('メールアドレスを入力してください。');

$('#registerEmail').focus();

return;

}

  

if (!/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {

alert('正しいメールアドレスの形式で入力してください。');

$('#registerEmail').focus();

return;

}

  

window.emailVerified = false;

  

$('#sendEmailCodeBtn').prop('disabled', true).text('送信中...');

$('#emailVerificationMessage').text('認証メールを送信しています...')

.removeClass('text-success text-danger').addClass('text-secondary');

  

$.ajax({

url: '${pageContext.request.contextPath}/member/sendEmailCode.do',

type: 'POST',

data: { email: email },

success: function (response) {

if (response.trim() === 'SUCCESS') {

$('#emailVerificationMessage').text('認証メールを送信しました。メールをご確認ください。')

.removeClass('text-danger text-secondary').addClass('text-success');

$('#sendEmailCodeBtn').prop('disabled', false).text('認証メール再送信');

} else {

$('#emailVerificationMessage').text('メール送信に失敗しました。アドレスを確認してください。')

.removeClass('text-success text-secondary').addClass('text-danger');

$('#sendEmailCodeBtn').prop('disabled', false).text('メール認証');

}

},

error: function () {

$('#emailVerificationMessage').text('サーバー通信エラーが発生しました。')

.removeClass('text-success text-secondary').addClass('text-danger');

$('#sendEmailCodeBtn').prop('disabled', false).text('メール認証');

}

});

});

  

/* 2. Email 인증번호 검증 AJAX (CheckEmailCodeController 연동) */

$('#verifyEmailCodeBtn').on('click', function () {

const inputCode = $.trim($('#emailVerificationCode').val());

  

if (!inputCode) {

alert('認証番号を入力してください。');

$('#emailVerificationCode').focus();

return;

}

  

$.ajax({

url: '${pageContext.request.contextPath}/member/checkEmailCode.do',

type: 'POST',

data: { inputCode: inputCode },

success: function (response) {

if (response.trim() === 'MATCH') {

window.emailVerified = true;

  

$('#emailVerificationCode').removeClass('is-invalid').addClass('is-valid');

$('#verifyEmailCodeBtn').prop('disabled', true).text('認証済み');

$('#sendEmailCodeBtn').prop('disabled', true);

  

$('#emailVerificationMessage').text('メール認証が完了しました。')

.removeClass('text-danger text-secondary').addClass('text-success');

} else {

window.emailVerified = false;

$('#emailVerificationCode').removeClass('is-valid').addClass('is-invalid');

$('#emailVerificationMessage').text('認証番号が一致しません。もう一度ご確認ください。')

.removeClass('text-success text-secondary').addClass('text-danger');

}

},

error: function () {

alert('認証番号の確認中にエラーが発生しました。');

}

});

});

  

/* 회원가입 Submit (최종 DB 전송) */

$('#registerForm').on('submit', function (e) {

e.preventDefault();

  

const id = $.trim($('#registerId').val());

if (!id) {

alert('アイディーを入力してください.');

$('#registerId').focus();

return false;

}

  

const password = $('#registerPassword').val();

if (!password || password.length < 8) {

alert('パスワードは8文字以上で入力してください.');

$('#registerPassword').focus();

return false;

}

  

const passwordConfirm = $('#registerPasswordConfirm').val();

if (password !== passwordConfirm) {

alert('パスワード（確認）が一致しません.');

$('#registerPasswordConfirm').focus();

return false;

}

  

const email = $.trim($('#registerEmail').val());

if (!email) {

alert('メールアドレスを入力してください.');

$('#registerEmail').focus();

return false;

}

  

if (!window.idChecked) {

alert('アイディーの重複チェックを行ってください。');

$('#registerId').focus();

return false;

}

  

if (!window.emailVerified) {

alert('メール認証を完了してください。');

return false;

}

  

// 모든 유효성 검사 통과 시 /member/join.do로 Form 데이터 전송

this.submit();

});

  

/* Reset */

$('#registerForm').on('reset', function () {

setTimeout(function () {

window.idChecked = false;

window.emailVerified = false;

  

$('#idCheckMessage').text('').removeClass('text-success text-danger');

$('#emailVerificationCode').val('').removeClass('is-valid is-invalid');

$('#emailVerificationMessage').text('').removeClass('text-success text-danger text-secondary');

  

$('#sendEmailCodeBtn').prop('disabled', false).text('メール認証');

$('#verifyEmailCodeBtn').prop('disabled', false).text('確認');

$('#checkIdBtn').prop('disabled', false).text('重複チェック');

}, 0);

});

});

</script>

</body>

</html>