<script setup>
import ScoreTable from '@/views/ScoreTable.vue';
</script>

<template>
  <v-container id="main_card_wrapper" fluid>
    <v-card id="main_card">
      <h1>Space quiz !</h1>
      <p>Here is a little quiz on space and astronomy.</p>
      <v-btn to="/start-new-quiz" color="accent">
        Start the quiz now!
      </v-btn>
      <v-container id="scores_container" class="d-flex flex-column align-center"
        v-if="true || registeredScores && registeredScores.length > 0">
        <h1>High scores</h1>
        <ScoreTable id="score_table" />
      </v-container>
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
    // Get quioz info
    const response = await quizApiService.getQuizInfo();
    if (response === undefined) {
      console.error(`HomePage: Could not get quiz info`)
      return
    }
    this.registeredScores = response.data;
  }
};
</script>

<style scoped>
#score_table {
  width: max(250px, min(500px, 80%));
}
</style>