<template>
  <v-container>
    <v-card loading class="mx-auto my-12">
      <div class="card-content"> <!--hérite du style de HomePage-->
        <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }} :</h1>
        <QuestionDisplay :loading="loading" :question="currentQuestion"
          :currentAnswer="answers[currentQuestionPosition - 1]" @answer-selected="answerClickedHandler" />
        <v-btn :disabled="loading || !canGoBack()" @click="goBack()" icon="mdi-arrow-collapse-left"></v-btn>
        <v-btn :disabled="loading || !canGoNext()" @click="goNext()" icon="mdi-arrow-collapse-right"></v-btn>
        <v-progress-circular v-if="loading" indeterminate></v-progress-circular>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import QuizApiService from '@/services/QuizApiService';
import ParticipationStorageService from '@/services/ParticipationStorageService';
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
      const postScoreRequest = await QuizApiService.postScore(ParticipationStorageService.getPlayerName(), this.answers)
      this.verifyCorrectness(postScoreRequest)
      const score = postScoreRequest.data.score
      ParticipationStorageService.saveParticipationScore(score)
      this.$router.push("/score-page")
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
