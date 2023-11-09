<template>
  <div class="wrapper">
    <div class="container">
      <div class="half-header"><h1>Quiz 퀴즈</h1></div>
      <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
    </div>

    <nav>
      <RouterLink :to="{ name: 'home' }">Home | </RouterLink>
      <RouterLink :to="{ name: 'quiz' }">Quiz | </RouterLink>
    </nav>
  </div>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>
.wrapper {
  margin: 0 auto;
  margin-bottom: 10%;
  text-align: center;
  background-color: lightgray;
  width: 600px;
  height: 300px;
  padding: 2%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.container {
  margin: 0 auto;
  background-color: white;
  border-radius: .5rem;
  height: 200px;
}
.container > p {
  padding: 0 1rem;

}
.half-header {
  color: white;
  margin: 0 auto;
  /* width: auto; */
  background-color: orange;
  display: flex;
  text-align: center;
  align-items: center;
  height: 70px;
  border-top-left-radius: .5rem;
  border-top-right-radius: .5rem;
  padding: 0 1rem;

}
nav {
  color: white;
  background-color: #000; /* 검은 바탕색상 */
  padding: 10px; /* 원하는 내부 여백 */
  border-radius: .5rem;
}

</style>
