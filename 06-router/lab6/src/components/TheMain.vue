<template>
  <div class="container">
    <h2>퀴즈 앱 사용 방법</h2>
    <div>
      <h1>1. 퀴즈 목록 확인하기</h1>
      <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요</p>
      <div class="img-container">
        <img src="../assets/assets/quizList.png" alt="">
        <img src="../assets/assets/quizCreate.png" alt="">
        <img src="../assets/assets/quizAnswer.png" alt="">
      </div>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.container {
  width: 1000px;
  margin: 0 auto; /* 가운데 정렬 */
  margin-top: 5%;
}

.image-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

img {
  width: 1000%; /* 가로 폭 100%로 설정 */
  max-width: 1000px; /* 최대 폭 설정 */
  margin-bottom: 10px; /* 이미지 간 여백 설정 */
}
</style>