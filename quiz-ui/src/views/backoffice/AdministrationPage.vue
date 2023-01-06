<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-card-title>Administration Page</v-card-title>
      <question-list/>
    </v-card>
  </v-container>
</template>
<script>
import StorageService from '@/services/StorageService';
import QuestionList from './QuestionList.vue';
export default {
  components: { QuestionList },
  beforeCreate(){
    const token = StorageService.getToken()
    if (!token){
      this.$router.push("/login")
    }
  },
}
</script>