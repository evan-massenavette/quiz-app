<template>
  <v-card>
    <v-form
        v-model="form"
        @submit.prevent="login"
      >
    <h1>Admin Login</h1>
    <v-text-field
      prepend-icon="mdi-account"
      type="password"
      label="Password"
      clearable
      placeholder="Enter your password"
      :rules="[required]"
      :readonly="loading"
      v-model="password">
    </v-text-field>
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
export default {
  name: "LoginPage",
  data() {
    return {
      form: false,
      loading: false,
      password: '',
    };
  },
  methods: {
    login() {
      if (!this.form) return
      this.loading=true
      console.log("fonction login a rajouté ici")
      this.loading=false
    },
    required(v){
      return !!v || 'Required'
    },
  }
};
</script>