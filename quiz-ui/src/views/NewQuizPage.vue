<template>
  <v-card>
    <h1>Player Information</h1>
    <v-form
      v-model="form"
      @submit.prevent="launchNewQuiz"
    >
      <v-text-field
        prepend-icon="mdi-account"
        type="text"
        label="Username"
        clearable
        placeholder="Enter your username"
        :rules="rules"
        :readonly="loading"
        v-model="username"
      ></v-text-field>
      <v-btn 
        :disabled="!form"
        :loading="loading"
        type="submit"
        color="success"
        size="large"
        block
        variant="elevated"
      >Login</v-btn>
    </v-form>
  </v-card>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      form: false,
      loading: false,
      username: '',
      rules: [
        value => !!value || 'Required',
        value => (value && value.length >= 3) || 'At least 3 characters',
      ],
    };
  },
  methods: {
    launchNewQuiz() {
      if (!this.form) return
      this.loading=true
      participationStorageService.savePlayerName(this.username);
      this.loading=false
      this.$router.push('/questions');
    },
  }
};
</script>