<template>
  <div class="header">
    <h2>귀여운 랜덤 갱얼쥐</h2>
    <button @click="getRandomDogData">새로운 큐트퍼피 소환하기</button>
  </div>
  <!-- {{ dogs }} -->
  <div v-if="dogIsEmpty" class="dog-container">
    <div v-for="dog in dogs" class="dog-box">
      <DogDetail :dog="dog"/>
    </div>
  </div>
  <div v-else>
    아직 갱얼쥐가 도착하지 않았습니다
  </div>
</template>

<script setup>
import { computed, watch } from "vue";
import DogDetail from '@/components/DogDetail.vue'

const emit = defineEmits(['getDogData'])

const getRandomDogData = () => {
  emit('getDogData')
}

const props = defineProps({
  dogs: Array   
})

// console.log(props.dogs) script에서는 props.<변수>로 접근
const dogIsEmpty = computed(() => {
  return props.dogs.length > 0 ? true : false
})
</script>

<style scoped>
  .header {
    display: flex;
    justify-content: space-between;
  }
  .dog-container {
    border: 1px solid black;
    justify-content: space-between;
    margin-top: 10%;
  }
  .dog-box {
    border: 1px solid black;
    margin: 10px;
    border-radius: 10px;
    display: flex;
  }
</style>