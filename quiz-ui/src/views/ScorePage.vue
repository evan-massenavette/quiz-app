<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <div class="card-score-content">
        <v-card-title class="card-score-title">Score Page</v-card-title>

        <v-card-text>
          <p class="text-h3 text--primary">Actual score: {{ yourScore }} / {{ totalScore }}</p>
          <p class="text-h5 text--primary"> Highest score: {{ highestScore }} / {{ totalScore }}</p>
        </v-card-text>

        <v-divider></v-divider>

        <v-btn-toggle v-model="toggle_exclusive">
          <v-btn variant="outlined" mandatory>High scores</v-btn>
          <v-btn variant="outlined">Your score</v-btn>
        </v-btn-toggle>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import QuizApiService from '@/services/QuizApiService';
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "ScorePage",
  data() {
    return {
      yourScore: 0,
      totalScore: 0,
      registeredScores: [],
      highestScore: 0
    };
  },
  async created() {
    const result = await QuizApiService.getQuizInfo()
    if (!result.ok) {
      throw Error('Error while getting quiz info')
    }
    this.registeredScores = result.data;
    this.totalScore = result.data.size;
  },
  async participantScore() {
    this.yourScore = await participationStorageService.getParticipationScore();
  },
  async highestScore() {
    const allScores = this.registeredScores.map(x => x[1]);
    this.highestScore = allScores.reduce((a, b) => Math.max(a, b), -Infinity);
  }
};
</script>

<style>
.card-score-content {
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.card-score-title {
  font-size: x-large;
}

.text-h3 {
  text-align: center;
}

.text-h5 {
  text-align: center;
  margin: 20px;
}
</style>