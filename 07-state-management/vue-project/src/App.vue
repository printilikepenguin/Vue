<template>
  <div>
    <h1>Todo PJT</h1>
    <h3>완료된 Todo : {{ store.doneTodosCount }}</h3>
    <TodoForm />
    <TodoList />
    <Test />
  </div>

</template>

<script setup>
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';
import Test from '@/components/Test.vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()


</script>

<style scoped>

</style>