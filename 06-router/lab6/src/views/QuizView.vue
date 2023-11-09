<template>
  <QuizCreate />
  
  <div class="container">
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">
        <h3>1번 문제. Python 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?</h3>
        정답 입력
      </label>
      <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="바보야 넌 모르지">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">
        <h3>2번 문제. HTML에서 텍스트 입력란을 만드는데 사용되는 요소는?</h3>
        정답 입력
      </label>
      <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="바보야 넌 모르지">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">
        <h3>3번 문제. 웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?</h3>
        정답 입력
      </label>
      <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="바보야 넌 모르지">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">
        <h3>4번 문제. Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?</h3>
        정답 입력
      </label>
      <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="바보야 넌 모르지">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">
        <h3>5번 문제. 웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇일까요?</h3>
        정답 입력
      </label>
      <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="바보야 넌 모르지">
    </div>
  </div>
</template>

<script setup>
import QuizCreate from '@/components/QuizCreate.vue'

</script>

<style>
.container {
}
.mb-3 {
  background-color: rgb(243, 243, 243);
  border: solid 1px lightgray;
  padding: 2%;
  border-radius: .5rem;

}
</style>