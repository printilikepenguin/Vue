<script setup>
import SingerDetail from '@/components/Singers/SingerDetail.vue'

const singers = [
  { id: 1, name: 'adele' },
  { id: 2, name: 'maroon5' },
  { id: 3, name: 'Dua Lipa' }
];
</script>

<template>
  <h1>가수 목록</h1>
  <SingerDetail v-for="singer in singers" :key="singer.id" :singer="singer" />
</template>

<style scoped>
h1 {
  text-align: center;
  color: orangered;
}
</style>
