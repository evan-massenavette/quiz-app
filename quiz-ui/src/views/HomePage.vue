<script setup>
import ScoreTable from '@/views/ScoreTable.vue';
</script>

<template>
  <v-container id="main_card_wrapper" fluid>
    <v-card id="main_card">
      <h1>Space quiz !</h1>
      <p>
        Here is a little quiz on space and astronomy !
        How many can you get right out of {{ questionsAmount }} ?
      </p>
      <v-btn to="/start-new-quiz" color="accent">
        Start the quiz now!
      </v-btn>
      <v-container class="d-flex flex-column align-center" v-if="highestScores && highestScores.length > 0">
        <h1>Highest Scores</h1>
        <ScoreTable :scores-and-ranks="highestScores" class="score_table_size" />
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import ScoresService from '@/services/ScoresService';

export default {
  name: "HomePage",
  data() {
    return {
      highestScores: [],
      questionsAmount: 0,
    };
  },
  async created() {
    // Get quiz info
    const response = await QuizApiService.getQuizInfo();
    if (response === undefined) {
      console.error(`HomePage: Could not get quiz info`)
      return
    }

    // Extract data from quiz info
    this.questionsAmount = response.data.size;
    this.highestScores = response.data.scores;

    // Get the highest scores and add rank for each particiation
    ScoresService.sort(this.highestScores);
    ScoresService.addRanks(this.highestScores);
  }
};
</script>
