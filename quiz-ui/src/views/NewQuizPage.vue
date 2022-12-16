<template>
  <div class="about">
    <p>Saisissez votre nom :</p>
    <input type="text" v-model="username"/>
    <button @click="launchNewQuiz">GO!</button>
  </div>
</template>
<script>
export default {
  name: "New Quiz Page",
  data() {
    return {
      username: '',
    };
  },
  methods:{
    launchNewQuiz(){
      console.log("Launch new quiz with", this.username);
    },
  }
};
</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
