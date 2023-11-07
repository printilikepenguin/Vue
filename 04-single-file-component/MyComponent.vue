<!-- vbase 탭, 셋업 -->

<template>
  <div class="greeting">
    {{ msg }}
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('hello world!')
</script>

<!-- scoped는 템플릿에만 쓸 거라고 묶어주는 것 -->
<!-- 스타일은 여러개가 될 수 있음 -->
<style scoped>
.greeting {
  color: aquamarine;
}
</style>