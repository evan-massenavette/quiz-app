<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <div class="card-content">
        <h1>Home page</h1>
        <div class="quiz-description">
          <p>Here is a little quiz on space and astronomy.</p>
        </div>
        <RouterLink class="router-link-quiz" to="/start-new-quiz-page">Start the quiz now!</RouterLink>
      </div>
    </v-card>
    <v-card class="mx-auto my-12" v-if="registeredScores && registeredScores.length > 0">
      <div class="card-content">
        <h1>High scores</h1>
        <div class="quiz-description">
          <p>Look at the best entries.</p>
        </div>
        <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
        </div>
      </div>
    </v-card>
  </v-container>
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

<style>
.card-content {
  margin-left: 20px;
  margin-right: 20px;
  margin-top: 10px;
  margin-bottom: 20px;
}

.quiz-description {
  margin-top: 10px;
  margin-bottom: 10px;
}

.router-link-quiz {
  display: inline-block;
  width: 150px;
  height: 30px;
  font-size: large;
  color: hsl(228, 87%, 52%);
  align-items: center;
  justify-content: center;
}

.router-link-quiz:hover {
  background-color: white;
}
</style>