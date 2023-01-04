<template>
  <v-card>
    <p>Saisissez votre nom :</p>
    <v-text-field label="Nom"
      :rules="rules"
      v-model="username" />
    <v-btn @click="launchNewQuiz">GO!</v-btn>
  </v-card>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      form: false,
      username: '',
      rules: [
        value => !!value || 'Required',
        value => (value && value.length >= 3) || 'At least 3 characters',
      ],
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  }
};
</script>