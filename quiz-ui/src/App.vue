<script setup>
import { RouterView } from 'vue-router'
import Header from '@/views/PageHeader.vue'
</script>

<template>
  <v-app>
    <Header />

    <v-main>
      <v-parallax src="src/assets/images/space_background.jpg">
        <RouterView />
      </v-parallax>
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
  top: 0px;
  left: 0px;
  position: fixed;
  width: 100%;
  height: 100%;
}
</style>