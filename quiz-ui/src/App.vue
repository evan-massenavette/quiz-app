<script setup>
import { RouterView } from 'vue-router'
import Header from '@/views/Header.vue'
</script>

<template>
  <v-app>
    <Header />
    <v-main class="v-main">
      <RouterView class="main_router_view" />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App'
};
</script>


<style>
@import '@/assets/main.css';

.v-main {
  background-image: url('@/assets/images/space_background.jpg');
  background-size: cover;
}

.main_router_view {
  border: 1px solid blue;
}
</style>