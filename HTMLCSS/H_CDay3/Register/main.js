// 함수 정의
function submitForm() {
    // value 속성으로 입력 값 가져오기
    const id = document.getElementById('userId').value;
    const pw = document.getElementById('userPw').value;
    const email = document.getElementById('userEmail').value;
  
    // 인수와 반환 예시: 값 확인 함수 호출
    const message = validateForm(id, pw, email);
  
    // 결과 출력
    document.getElementById('result').innerText = message;
  }
  
  // 인수와 반환을 활용한 유효성 검사 함수
  function validateForm(id, pw, email) {
    if (!id || !pw || !email) {
      return "모든 항목을 입력해주세요.";
    }
    if (pw.length < 6) {
      return "비밀번호는 6자 이상이어야 합니다.";
    }
    return `회원가입 완료! 환영합니다, ${id}님.`;
  }
  