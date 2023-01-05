<script setup>
import ScoreTable from '@/views/ScoreTable.vue';
</script >

<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <div class="card-score-content">
        <v-card-title class="card-score-title">Score Page</v-card-title>

        <v-card-text>
          <p class="text-h3 text--primary">Actual score: {{ yourScore }} / {{ totalScore }}</p>
          <p class="text-h5 text--primary"> Highest score: {{ highestScore }} / {{ totalScore }}</p>
        </v-card-text>

        <v-btn-toggle v-model="toggle_one" shaped mandatory>
          <v-btn variant="outlined" @click="buttonHighScore">High scores</v-btn>
          <v-btn variant="outlined" @click="buttonYourScore">Your score</v-btn>
        </v-btn-toggle>

        <v-card>
          <v-card v-if="revealHighScore">
            <v-container id="scores_container" v-if="true || registeredScores && registeredScores.length > 0">
              <ScoreTable id="score_table" />
            </v-container>
          </v-card>
          <v-expand-transition>
            <v-card v-if="revealYourScore">
              <p>Mettre le tableau 2</p>
            </v-card>
          </v-expand-transition>
        </v-card>
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
      registeredScores: [],
      yourScore: 0,
      totalScore: 0,
      highestScore: 0,
      toggle_one: 0,
      revealHighScore: true,
      revealYourScore: false
    };
  },
  async created() {
    const result = await QuizApiService.getQuizInfo()
    if (result.status != 200) {
      throw Error('Error while getting quiz info')
    }
    this.registeredScores = result.data;
    this.totalScore = result.data.size;

    this.getParticipantScore();
    this.getHighestScore();
  },
  methods: {
    async getParticipantScore() {
      this.yourScore = await participationStorageService.getParticipationScore();
    },
    getHighestScore() {
      const allScores = this.registeredScores.map(x => x[1]);
      this.highestScore = allScores.reduce((a, b) => Math.max(a, b), -Infinity);
    },
    buttonHighScore() {
      this.revealHighScore = true;
      this.revealYourScore = false;
    },
    buttonYourScore() {
      this.revealHighScore = false;
      this.revealYourScore = true;
    }
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