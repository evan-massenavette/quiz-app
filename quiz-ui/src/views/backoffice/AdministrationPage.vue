<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-card-title>Administration Page</v-card-title>
      <QuestionList/>
    </v-card>
  </v-container>
</template>
<script>
import AuthService from '@/services/AuthService';
import QuestionList from './QuestionList.vue';

export default {
    beforeCreate() {
        if (!AuthService.isAuthenticated())
            this.$router.push("/login");
    },
    components: { QuestionList }
}
</script>