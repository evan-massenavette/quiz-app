<template>
  <v-container id="main_card_wrapper" fluid>
    <v-card id="main_card">
      <v-form class="v-form" v-model="form" @submit.prevent="launchNewQuiz">
        <v-card-title>Enter your name:</v-card-title>
        <v-card-text>
          <v-text-field
            prepend-icon="mdi-form-textbox"
            type="text"
            label="Name"
            clearable
            placeholder="Enter your name"
            :rules="rules"
            :readonly="loading"
            v-model="username"
          />
        </v-card-text>
        <v-card-actions>
          <v-btn
            id="go_button"
            :disabled="!form"
            :loading="loading"
            type="submit"
            block
            >GO!</v-btn
          >
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>
<style scoped>
.v-form {
  width: 100%;
}
</style>
<script>
import StorageService from "@/services/StorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      form: false,
      loading: false,
      username: "",
      rules: [
        (value) => !!value || "Required",
        (value) => (value && value.length >= 3) || "At least 3 characters",
        (value) =>
          (value && value.length <= 50) || "No more than 50 characters",
      ],
    };
  },
  methods: {
    launchNewQuiz() {
      if (!this.form) return;
      this.loading = true;
      StorageService.clear();
      StorageService.savePlayerName(this.username);
      this.loading = false;
      this.$router.push("/questions");
    },
  },
};
</script>

<style>
#go_button {
  background-color: rgb(var(--v-theme-accent));
  width: fit-content;
}
</style>
