<template>
  <nav class="nav">
    <RouterLink :to="{name: 'main'}">main</RouterLink>
    <RouterLink :to="{name: 'product'}">product</RouterLink>
    <RouterLink :to="{name: 'map'}">map</RouterLink>
    <RouterLink :to="{name: 'article'}">article</RouterLink>
    <RouterLink :to="{name: 'exchange'}">exchange</RouterLink>
    <!-- <RouterLink :to="{name: 'user'}">user</RouterLink> -->
  </nav>

  <RouterView />

</template>

<script setup>

</script>

<style scoped>
.nav {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #333;
  color: white;
  padding: 10px;
}

.nav a {
  text-decoration: none;
  color: white;
  padding: 8px;
  border-radius: 5px;
}

.nav a:hover {
  background-color: #555;
}
</style>