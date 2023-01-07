<script setup>
import { RouterLink } from "vue-router";
import AuthService from "@/services/AuthService";
</script>

<template>
  <v-app-bar height="50" color="surface">
    <RouterLink class="header_button" to="/">
      <v-icon icon="mdi-home" />
      <p>Home</p>
    </RouterLink>
    <v-divider vertical class="header_divider" />

    <v-spacer />
    <v-img src="logo.svg" />
    <v-spacer />

    <v-divider vertical class="header_divider" />
    <RouterLink to="/administration" class="header_button" v-if="loggedIn">
      <v-icon icon="mdi-lead-pencil" />
      <p>Edit Quiz</p>
    </RouterLink>

    <v-divider vertical class="header_divider" />
    <RouterLink
      to="/login"
      class="header_button"
      v-if="loggedIn"
      @click="logout()"
    >
      <v-icon icon="mdi-login-variant" />
      <p>Admin Logout</p>
    </RouterLink>
    <RouterLink to="/login" class="header_button" v-if="!loggedIn">
      <v-icon icon="mdi-login-variant" />
      <p>Admin Login</p>
    </RouterLink>
  </v-app-bar>
</template>

<style scoped>
.header_button {
  height: 100%;
  color: rgb(var(--v-theme-text-surface));
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 10px;
}

.header_button > p {
  margin-left: 5px;
}

.header_button:hover {
  color: rgb(var(--v-theme-accent));
  background-color: rgb(var(--v-theme-surface-darken-1));
}

.header_divider {
  background-color: rgb(var(--v-theme-surface-lighten-1));
}
</style>

<script>
export default {
  name: "PageHeader",
  data() {
    return {
      loggedIn: false,
    };
  },
  methods: {
    loginCallback() {
      this.loggedIn = true;
    },
    logout() {
      this.loggedIn = false;
      AuthService.logout();
      this.$router.push("/");
    },
  },
  created() {
    // Set loggedIn flag
    this.loggedIn = AuthService.isAuthenticated();

    // Register login callback
    AuthService.setLoginCallback(this.loginCallback);
  },
};
</script>
