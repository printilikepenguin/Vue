<template>
  <div v-if="dogIs">
    <img :src="props.dog.url" alt="강아지의 사진">
      <div v-if="dog.detail" class="dog-info">
        <p><strong>이름: </strong>{{ dog.detail.name }}</p>
        <p><strong>품종: </strong>{{ dog.detail.breed_group }}</p>
        <p><strong>높이:</strong> {{ dog.detail.height.imperial }} 인치 ({{ dog.detail.height.metric }} cm)</p>
        <p><strong>수명:</strong> {{ dog.detail.life_span }}</p>
        <p><strong>성격:</strong> {{ dog.detail.temperament }}</p>
        <p><strong>무게:</strong> {{ dog.detail.weight.imperial }} 파운드 ({{ dog.detail.weight.metric }} kg)</p>
      </div>
      <div v-else class="dog-info">
        상세 정보 없음 ㅜㅜ
      </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
const props = defineProps({
  dog: Array   
})

const dogIs = computed(() => {
  return props.dog.length > 0 ? true : false
})


</script>

<style scoped>
  img {
    width: 200px;
    height: 200px;
    object-fit: fill;
    border-radius: 10px;
  }


</style>