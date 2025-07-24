function attackMonster() {
    const hpBar = document.getElementById("HPbar");
    const consoleDiv = document.getElementById("consoles");

    // 1~10 사이의 랜덤한 데미지 생성
    const damage = Math.floor(Math.random() * 10) + 1;

    // 현재 HP 가져오기
    let currentHP = parseInt(hpBar.value);

    // HP에서 데미지 만큼 감소 (0 이하로 떨어지지 않게)
    currentHP = Math.max(currentHP - damage, 0);

    // 새로운 HP 반영
    hpBar.value = currentHP;

    // 로그 출력
    consoleDiv.innerHTML += `<p>몬스터에게 ${damage} 데미지를 입혔습니다! 남은 HP: ${currentHP}</p>`;

    // 몬스터가 죽었을 때
    if (currentHP === 0) {
        consoleDiv.innerHTML += `<p><strong>몬스터를 쓰러뜨렸습니다!</strong></p>`;
    }
}
