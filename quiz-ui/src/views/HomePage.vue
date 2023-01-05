<template>
  <v-container id="main_card_wrapper">
    <v-card id="main_card">
      <h1>Space quiz !</h1>
      <p>Here is a little quiz on space and astronomy.</p>
      <v-btn id="goto_quiz_button" to="/start-new-quiz-page" ripple="false">
        Start the quiz now!
      </v-btn>
      <v-container v-if="true || registeredScores && registeredScores.length > 0">
        <h1>High scores</h1>
        <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
        </div>
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
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
        },
        {
          name: 'Eclair',
          calories: 262,
        },
        {
          name: 'Cupcake',
          calories: 305,
        },
        {
          name: 'Gingerbread',
          calories: 356,
        },
        {
          name: 'Jelly bean',
          calories: 375,
        },
        {
          name: 'Lollipop',
          calories: 392,
        },
        {
          name: 'Honeycomb',
          calories: 408,
        },
        {
          name: 'Donut',
          calories: 452,
        },
        {
          name: 'KitKat',
          calories: 518,
        },
      ]
    };
  },
  async created() {
    this.registeredScores = await quizApiService.getQuizInfo().data;
  }
};
</script>

<style scoped>
#main_card_wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
}

#main_card {
  padding: 10px 20px;
  width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
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
</style>