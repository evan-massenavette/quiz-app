<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <div class="card-content"> <!--hérite du style de HomePage-->
        <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }} :</h1>
        <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
        <v-btn :disabled="!canGoBack()" @click="goBack()" icon="mdi-arrow-collapse-left"></v-btn>
        <v-btn :disabled="!canGoNext()" @click="goNext()" icon="mdi-arrow-collapse-right"></v-btn>
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
    const quizInfoRequest=await QuizApiService.getQuizInfo()
    this.verifyCorrectness(quizInfoRequest)
    this.totalNumberOfQuestion = quizInfoRequest.data.size;

    // Launch the quiz
    this.loadQuestionByPosition();
  },
  data() {
    return {
      currentQuestion: {"text": "", "title": "", "image": "", possibleAnswers:[]},
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0,
      answers: []
    };
  },
  methods: {
    canGoBack(){
      return this.currentQuestionPosition>1
    },
    canGoNext(){
      return this.answers[this.currentQuestionPosition-1]!==undefined
    },
    goBack(){
      this.currentQuestionPosition--;
      this.loadQuestionByPosition();
    },
    goNext(){
      this.currentQuestionPosition++;
      this.loadQuestionByPosition();
    },
    async answerClickedHandler(answerIndex) {
      this.answers[this.currentQuestionPosition-1]=answerIndex;
      this.currentQuestionPosition++;
      this.loadQuestionByPosition();
    },
    async endQuiz() {
      const postScoreRequest = await QuizApiService.postScore(ParticipationStorageService.getPlayerName(), this.answers)
      this.verifyCorrectness(postScoreRequest)
      const score = postScoreRequest.data.score
      ParticipationStorageService.saveParticipationScore(score)
      this.$router.push("/score")
    },
    async loadQuestionByPosition() {
      console.log(this.answers)
      if(this.currentQuestionPosition<=this.totalNumberOfQuestion){
        const questionRequest = await QuizApiService.getQuestion(this.currentQuestionPosition);
        this.verifyCorrectness(questionRequest)
        this.currentQuestion=questionRequest.data
      }
      else{
        this.endQuiz()
      }
      
    },
    manageError(status){
      this.$router.push(`/error/${status}`) 
    },
    verifyCorrectness(request){
      const status=request.status
      if(status!=200){
        this.manageError(status)
      }
    }
  }
}
</script>
