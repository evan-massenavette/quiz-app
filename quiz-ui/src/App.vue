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

<script>
export default {
  name: 'App'
};
</script>


<style>
@import '@/style/main.css';

.v-main {
  background-image: url('@/assets/images/space_background.jpg');
  background-size: cover;
}
</style>