<template>
  <v-card>
    <h1>Home page</h1>
    <p>Petite description du quiz pour savoir de quoi ça parle et donner envie d'y jouer</p>

    <RouterLink to="/start-new-quiz-page">Démarrer le quiz !</RouterLink>

    <p>Top scores (ça ne s'affiche pas encore en dessous)</p>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
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
    console.log("Composant Home page 'created'");
  }
};
</script>