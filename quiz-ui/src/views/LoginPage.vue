<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-form v-model="form" @submit.prevent="login">
        <v-card-title>Admin Login</v-card-title>
        <v-card-text>
          <v-text-field prepend-icon="mdi-form-textbox-password" type="password" label="Password" clearable
            placeholder="Enter your password" :rules="[required]" :readonly="loading" v-model="password">
          </v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn :disabled="!form" :loading="loading" type="submit" color="success" size="large" block
            variant="elevated">Login</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import StorageService from '@/services/StorageService';
import QuizApiService from '@/services/QuizApiService';
export default {
  beforeCreate(){
    const token = StorageService.getToken()
    if (token){
      this.$router.push("/administration")
    }
  },
  name: "LoginPage",
  data() {
    return {
      form: false,
      loading: false,
      password: '',
    };
  },
  methods: {
    async login() {
      if (!this.form) return
      this.loading = true
      const tokenRequest = await QuizApiService.login(this.password)
      if (tokenRequest.status===200){
        StorageService.saveToken(tokenRequest.data.token)
        this.$router.push('/administration');
      }
      this.loading=false
    },
    required(v) {
      return !!v || 'Required'
    },
  }
};
</script>