<template>
  <v-card>
    <h1>Home page</h1>
    <p>A little quiz about space and astronomy.</p>

    <RouterLink to="/start-new-quiz-page">Start the quiz now!</RouterLink>

    <div v-if="registeredScores && registeredScores.length>0">
      <p>High scores</p>
      <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
      </div>
    </div>
  </v-card>
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
  }
};
</script>