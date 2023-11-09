<template>
  <form class="wrapper">
  <div class="mb-3">
    <h3>퀴즈 생성</h3>

    <div class="container">
      <label for="InputQuiz" class="form-label">문제</label>
      <div class="form-floating">
        <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
        <label for="floatingTextarea2"></label>
      </div>
      
      <label for="InputAnswer" class="form-label">답안</label>
      <input type="answer" class="form-control" id="InputAnswer">
      
      <div class="d-grid gap-2" style="margin-top: 5%;">
        <button type="submit" class="btn btn-primary" @click="$emit('create-quiz')">퀴즈 생성</button>
      </div>
    </div>
    
  </div>
</form>
</template>

<script setup>
import { ref } from "vue";
defineEmits(['createQuiz'])

id = ref(1)
const newQuiz = {
  id: id,
  quiz: textarea.value,
  answer: input.value
}

</script>

<style scoped>
h3 {
  margin: 3% auto;
}
.wrapper {
  margin: 0 auto;
  margin-bottom: 10%;
  width: 600px;
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.container {
  margin: 5% auto;
}
</style>