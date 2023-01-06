<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-card-title>Administration Page</v-card-title>
    </v-card>
  </v-container>
</template>
<script>
import StorageService from '@/services/StorageService';
export default {
  beforeCreate(){
    const token = StorageService.getToken()
    if (!token){
      this.$router.push("/login")
    }
  },
}
</script>