<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-form v-model="form" @submit.prevent="launchNewQuiz">
        <v-card-title>Enter your name:</v-card-title>
        <v-card-text>
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Name" clearable placeholder="Enter your name"
            :rules="rules" :readonly="loading" v-model="username" />
        </v-card-text>
        <v-card-actions>
          <v-btn :disabled="!form" :loading="loading" type="submit">GO!</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import StorageService from "@/services/StorageService";

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
        value => (value && value.length <= 50) || 'No more than 50 characters'
      ],
    };
  },
  methods: {
    launchNewQuiz() {
      if (!this.form) return
      this.loading = true
      StorageService.clear();
      StorageService.savePlayerName(this.username);
      this.loading = false
      this.$router.push('/questions');
    },
  }
};
</script>

<style>
.v-btn {
  color: black;
  font-size: large;
  border-width: thin;
}
</style>