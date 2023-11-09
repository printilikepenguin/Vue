<template>
  <div>
    <h1>UserView</h1>
    <h3>{{ userId }} 유저의 페이지 입니다.</h3>
    <button @click="goHome">홈으로!</button>
    <button @click="goAnotherUser">100번 유저 페이지로!</button>
    <hr>
    <h3>{{ $route.params.id }} 유저의 페이지 입니다.</h3>
    <hr>
    <h3>{{ $route }} 유저의 페이지 입니다.</h3>
    <!-- route 출력하면 객체 전체가 뜸 -->

  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from "vue-router";

const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()
const goHome = function () {
  // router.push({ name: 'home' })
  router.replace({ name: 'home' })
}

// In-component Guard
// 1. 
onBeforeRouteLeave((to, from) => {
  window.confirm('정말 떠나실건가요')
  if (answer === false) {
    return false
  }
})

// 2. onBeforeRouteUpdate
const goAnotherUser = function () {
  router.push({name: 'user', params: {id: 100}})
}

// 이거 안하면 id 변동 안돼용
onBeforeRouteUpdate((to, from) => {
  console.log(to.params.id)
  userId.value = to.params.id
})

</script>

<style scoped>

</style>