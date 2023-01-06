<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <v-app-bar id="header" height="50">
    <RouterLink class="header_link" to="/">
      <v-icon icon="mdi-home" />
      <p>Home</p>
    </RouterLink>
    <v-divider vertical class="header_divider" />
    <v-spacer />
    <v-img src="src/assets/images/logo.svg" />
    <v-spacer />
    <v-divider vertical class="header_divider" />
    <RouterLink class="header_link" to="/login">
      <v-icon icon="mdi-login-variant" />
      <p>Admin login</p>
    </RouterLink>
  </v-app-bar>
</template>

<style scoped>
#header {
  padding: 0;
  background-color: rgb(var(--v-theme-surface));
}

.header_link {
  height: 100%;
  color: rgb(var(--v-theme-text-surface));
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 15px;
}

.header_link:hover {
  color: rgb(var(--v-theme-accent));
  background-color: rgb(var(--v-theme-surface-darken-1));
}

.header_divider {
  background-color: rgb(var(--v-theme-surface-lighten-1));
}
</style>