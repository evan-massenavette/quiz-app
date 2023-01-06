<template>
  <v-container id="main_card_wrapper" fluid>
    <v-card id="main_card">
      <v-form class="v-form" v-model="form" @submit.prevent="login">
        <h1>Admin Login</h1>
        <v-card color="error" v-if="this.errorMessage" class="text-center pa-2 mt-2">{{ this.errorMessage }}</v-card>
        <v-card-text>
          <v-text-field prepend-inner-icon="mdi-form-textbox-password" variant="outlined" type="password"
            label="Password" clearable placeholder="Enter your password" :rules="[required]" :readonly="loading"
            v-model="password">
          </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn :disabled="!form" :loading="loading" type="submit" color="accent" size="large" block
            variant="elevated">Login</v-btn>
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
import AuthService from '@/services/AuthService';

export default {
  beforeCreate() {
    if (AuthService.isAuthenticated()) this.$router.push('/administration')
  },
  name: 'LoginPage',
  data() {
    return {
      form: false,
      loading: false,
      errorMessage: '',
      password: '',
    };
  },
  methods: {
    async login() {
      if (!this.form) return;
      this.loading = true;
      try {
        await AuthService.login(this.password);
      }
      catch (e) {
        this.errorMessage = e.message;
        this.loading = false;
        return;
      }
      this.$router.push('/administration');
      this.loading = false;
    },
    required(v) {
      return !!v || 'Required'
    },
  }
};
</script>