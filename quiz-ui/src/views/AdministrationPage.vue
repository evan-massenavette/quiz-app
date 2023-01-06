<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-card-title>Administration Page</v-card-title>
    </v-card>
  </v-container>
</template>
<script>
import AuthService from '@/services/AuthService';

export default {
  beforeCreate() {
    if (!AuthService.isAuthenticated()) this.$router.push('/login')
  },
}
</script>