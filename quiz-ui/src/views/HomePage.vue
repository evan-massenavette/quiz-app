<template>
  <h1>Home page</h1>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>

  <RouterLink to="/start-new-quiz-page">Démarrer le quiz !</RouterLink>

</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    this.registeredScores = await quizApiService.getQuizInfo().data;
    console.log("Composant Home page 'created'");
  }
};
</script>