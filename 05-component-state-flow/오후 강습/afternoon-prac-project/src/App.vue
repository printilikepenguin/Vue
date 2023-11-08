<script setup>
import { ref } from "vue";
import DogList from "@/components/DogList.vue";
import axios from 'axios'

const dogs = ref([])

// async: 이 함수가 비동기 함수라고 알려주는 코드
// await: 비동기 함수의 종료를 기다려주는 키워드
// try-catch와 함께 자주 사용된다
const getDogData = async () => {
  const URL = 'https://api.thedogapi.com/v1/images/search?limit=10'
  // 버그 해결 코드
  try {
    const response = await axios.get(URL)
    
    const dogData = response.data

    // 암기1. 비동기 쓸 때 forEach 쓰지 말자...
    //   => map으로 변경: 기존 데이터를 토대로 새로운 배열 반환
    // 암기2. map 안에 async 쓰면 자동으로 Promise 객체 리턴
    const details = dogData.map(async (dog) => {
      const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
      const detailres = await axios.get(detailURL)
      dog.detail = detailres.data.breeds ? detailres.data.breeds[0] : null
    })
    
    // promise 객체 10개 출력됨 - 상태가 fulfilled(성공했다)
    // => 실행은 성공했는데 순서는 보장하지 못했다
    console.log(details)

    // Promise.all: 프로미스 배열의 계산이 모두 끝날때까지 기다려줌ㅍ
    await Promise.all(details)

    dogs.value = dogData
    console.log(dogData)

  } catch (error) {
    console.error('강아지 데이터 못불러옴', error)
  }

  // // 비동기 버그발생코드
  // axios.get(URL)
  //   .then((response) => {
  //     const dogData = response.data
  //     dogData.forEach((dog) => {
  //       const detailURL = `https://api.thedogapi.com/v1/images/${dog.id}`
  //       axios.get(detailURL)
  //       .then((response) => {
  //         // console.log('detail = ', response.data)
  //         dog.detail = response.data
  //       }).catch((error) => {
  //         console.error(error)
  //       })
  //     })
  //     dogs.value = dogData
  //     console.log(dogs.value)
  //   }).catch((error) => {
  //     console.error(error);
  //   })
}
</script>

<template>
  <div class="container">
    <h1>2023-11-08 실습</h1>
    <!-- DogList -->
    <!-- emit 이벤트 -->
    <!-- template -> 케밥-케이스 권장 -->
    <DogList :dogs="dogs" @get-dog-data="getDogData"/>
  </div>
</template>

<style scoped>
.container {
  width: 80%;
  margin: 0 auto;
  /* justify-content: center;
  text-align: center; */
}
</style>
