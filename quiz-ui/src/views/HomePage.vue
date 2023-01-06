<script setup>
import ScoreTable from '@/views/ScoreTable.vue';
</script >

<template>
  <v-container id="main_card_wrapper" fluid>
    <v-card id="main_card">
      <h1>Space quiz !</h1>
      <p>Here is a little quiz on space and astronomy.</p>
      <v-btn id="goto_quiz_button" to="/start-new-quiz-page">
        Start the quiz now!
      </v-btn>
      <v-container id="scores_container" v-if="true || registeredScores && registeredScores.length > 0">
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
    this.registeredScores = await quizApiService.getQuizInfo();
  }
};
</script>

<style scoped>
#main_card_wrapper {
  display: flex;
  justify-content: center;
  width: 100%;
}

#main_card {
  padding: 10px 20px;
  width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: fit-content;
}

#main_card h1 {
  text-align: center;
}

#main_card p {
  margin-top: 10px;
  margin-bottom: 10px;
}

#goto_quiz_button {
  background-color: rgb(var(--v-theme-accent));
  width: fit-content;
}

#scores_container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

#score_table {
  width: max(250px, min(500px, 80%));
}
</style>