<template>
  <div class="card">
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="열창하는 가수" />
    <p>가수 소개글 엔시티 짱!!!!!</p>
    <SingerAlbum />
    <SingerAlbum />
  </div>
</template>

<script setup>
import SingerAlbum from '@/components/Singers/SingerAlbum.vue'
</script>

<style scoped>
  .card {
    text-align: center;
    display: inline-block;
    width: 40%;
    outline: solid black 1px;
    padding: 3%;
    margin: 20px
  }
  img {
    width: 200px;
    border-radius: 70%;
  }
</style>

<!-- <style>
h1 {
  color: green;
}
</style> -->