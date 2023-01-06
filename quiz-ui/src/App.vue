<script setup>
import { RouterView } from 'vue-router'
import PageHeader from '@/views/PageHeader.vue'
</script>

<template>
  <v-app>
    <PageHeader />
    <v-main class="v-main">
      <RouterView />
    </v-main>
  </v-app>
</template>

<style>
/* 
Import main CSS in non-scoped style block 
so that all child components can access its content
*/
@import '@/style/main.css';
</style>

<style scoped>
.v-main {
  background-image: url('src/assets/images/space_background.jpg');
  background-size: cover;
}
</style>