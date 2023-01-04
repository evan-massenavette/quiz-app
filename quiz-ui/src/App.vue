<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <v-app>
    <v-app-bar app height="60">
      <template v-slot:prepend>
        <RouterLink class="router-link-home" to="/">
          <v-icon icon="mdi-home" />
          <p>Home</p>
        </RouterLink>
      </template>
      <v-spacer></v-spacer>
      <template v-slot:append>
        <RouterLink class="router-link-login" to="/login">
          <v-icon icon="mdi-account" />
          <p>Admin login</p>
        </RouterLink>
      </template>
    </v-app-bar>

    <v-main full-width>
      <v-parallax src="src/assets/Images/ivana-cajina-asuyh-_ZX54-unsplash.jpg">
        <v-container fluid>
          <RouterView />
        </v-container>
      </v-parallax>
    </v-main>

    <v-footer app height="47" color="black">Juste un test du footer
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
.router-link-home {
  display: inline-block;
  width: 90px;
  height: 50px;
  color: black;
  display: flex;
  align-items: center;
  justify-content: center;
}

.router-link-home:hover {
  color: #111166;
  background-color: #e4eaf7;
}

.router-link-login {
  display: inline-block;
  width: 130px;
  height: 50px;
  color: black;
  display: flex;
  align-items: center;
  justify-content: center;
}

.router-link-login:hover {
  color: #111166;
  background-color: #e4eaf7;
}
</style>