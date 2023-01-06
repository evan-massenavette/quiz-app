<script setup>
import ScoreTable from '@/views/frontoffice/ScoreTable.vue';
</script>

<template>
  <v-container id="main_card_wrapper">
    <v-card id="main_card">
      <h1>Actual score: {{ yourScore }} / {{ questionsAmount }}</h1>
      <h3>Highest score: {{ yourHighestScore }} / {{ questionsAmount }}</h3>

      <div class="score_table_size mt-5">
        <v-tabs v-model="scoresTab" fixed-tabs color="accent" bg-color="surface-lighten-1" density="comfortable">
          <v-tab key="highest_scores">Highest Scores</v-tab>
          <v-tab key="your_best_score">Your Best Score</v-tab>
        </v-tabs>

        <v-window v-model="scoresTab">
          <v-window-item key="highest_scores">
            <ScoreTable :scores-and-ranks="highestScores" />
          </v-window-item>
          <v-window-item key="your_best_score">
            <ScoreTable :scores-and-ranks="scoresNearYou" :highlighted-rank="yourRank" />
          </v-window-item>
        </v-window>
      </div>

      <v-btn to="/start-new-quiz" color="accent" class="mt-5">Try again</v-btn>

    </v-card>
  </v-container>
</template>

<style scoped>
.score_table {
  margin: 0 auto;
}
</style>

<script>
import QuizApiService from '@/services/QuizApiService';
import ScoresService from '@/services/ScoresService';
import StorageService from '@/services/StorageService';

export default {
  name: "ScorePage",
  data() {
    return {
      yourScore: 0,
      yourHighestScore: 0,
      yourRank: 0,
      highestScores: [],
      scoresNearYou: [],
      questionsAmount: 0,
      scoresTab: null,
    };
  },
  beforeCreate() {
    const score = StorageService.getParticipationScore();
    if (!score) this.$router.push("/")
  },
  async created() {
    // Get quiz info
    const response = await QuizApiService.getQuizInfo()
    if (response === undefined) {
      console.error(`HomePage: Could not get quiz info`)
      return
    }
    this.registeredScores = response.data.scores;
    this.questionsAmount = response.data.size;

    // Convert scores to appropriate form (sort and add ranks)
    ScoresService.sort(this.registeredScores);
    ScoresService.addRanks(this.registeredScores);

    // Get info for current user
    this.yourScore = ScoresService.getYourScore();
    this.yourHighestScore = ScoresService.getYourHighestScore(this.registeredScores);
    this.yourRank = ScoresService.getYourRank(this.registeredScores);

    // Get scores for tables
    this.highestScores = ScoresService.getHighestScores(this.registeredScores);
    this.scoresNearYou = ScoresService.getScoresNearYou(this.registeredScores);
  },
};
</script>
