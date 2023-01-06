<script setup>
import QuestionList from '@/views/backoffice/QuestionList.vue'
</script>

<template>
  <v-container id="main_card_wrapper">
    <v-card id="main_card">
      <h1>Administration Page</h1>
      <QuestionList />
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