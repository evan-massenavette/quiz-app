<template>
  <v-container id="main_card_wrapper" fluid>
    <v-card id="main_card">
      <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }} :</h1>
      <QuestionDisplay :loading="loading" :question="currentQuestion"
        :currentAnswer="answers[currentQuestionPosition - 1]" @answer-selected="answerClickedHandler" />
      <v-progress-circular class="margin-top" :class="{ hidden: !loading }" indeterminate></v-progress-circular>
      <div class="margin-top">
        <v-btn color="accent" :disabled="loading || !canGoBack()" @click="goBack()"
          icon="mdi-arrow-collapse-left"></v-btn>
        <v-btn color="accent" :disabled="loading || !canGoNext()" @click="goNext()"
          icon="mdi-arrow-collapse-right"></v-btn>
      </div>
    </v-card>
  </v-container>
</template>
<style scoped>
.margin-top {
  margin-top: 1em;
}

.hidden {
  visibility: hidden;
}
</style>
<script>
import QuizApiService from '@/services/QuizApiService';
import StorageService from '@/services/StorageService';
import QuestionDisplay from './QuestionDisplay.vue';

export default {
  components: {
    QuestionDisplay
  },
  async created() {
    // Get quiz info
    const quizInfoRequest = await QuizApiService.getQuizInfo()
    this.verifyCorrectness(quizInfoRequest)
    this.totalNumberOfQuestion = quizInfoRequest.data.size;

    // Launch the quiz
    this.loadQuestionByPosition();
  },
  data() {
    return {
      currentQuestion: { "text": "", "title": "", "image": "", possibleAnswers: [] },
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0,
      answers: [],
      loading: false
    };
  },
  beforeCreate() {
    const playerName = StorageService.getPlayerName();
    if (!playerName) this.$router.push("/")
  },
  methods: {
    canGoBack() {
      return this.currentQuestionPosition > 1
    },
    canGoNext() {
      return this.answers[this.currentQuestionPosition - 1] !== undefined
    },
    async goBack() {
      this.loading = true
      this.currentQuestionPosition--;
      await this.loadQuestionByPosition();
      this.loading = false
    },
    async goNext() {
      this.loading = true
      if (this.currentQuestionPosition === this.totalNumberOfQuestion) { // End if it's the end 
        await this.endQuiz()
      }
      else { // If not go to the next question
        this.currentQuestionPosition++;
        await this.loadQuestionByPosition();
      }
      this.loading = false
    },
    async answerClickedHandler(answerIndex) {
      this.answers[this.currentQuestionPosition - 1] = answerIndex;
      this.goNext();
    },
    async endQuiz() {
      const postScoreRequest = await QuizApiService.postScore(StorageService.getPlayerName(), this.answers)
      this.verifyCorrectness(postScoreRequest)
      const score = postScoreRequest.data.score
      StorageService.saveParticipationScore(score)
      this.$router.push("/score")
    },
    async loadQuestionByPosition() {
      if (this.currentQuestionPosition <= this.totalNumberOfQuestion && this.currentQuestionPosition > 0) { // Load question if it's possible
        const questionRequest = await QuizApiService.getQuestion(this.currentQuestionPosition);
        this.verifyCorrectness(questionRequest)
        this.currentQuestion = questionRequest.data
      }
    },
    manageError(status) {
      this.$router.push(`/error`)
    },
    verifyCorrectness(request) {
      const status = request.status
      if (status != 200) {
        this.manageError(status)
      }
    }
  }
}
</script>
