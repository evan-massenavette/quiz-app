<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuizApiService from '@/services/QuizApiService';
import QuestionDisplay from './QuestionDisplay.vue';
export default {
  components: {
    QuestionDisplay
  },
  async created() {
    this.totalNumberOfQuestion = await QuizApiService.getQuizInfo().data.size;
    if (this.totalNumberOfQuestion > 0) {
      this.loadQuestionByPosition();
    } else {
      this.endQuiz();
    }
  },
  data() {
    return {
      currentQuestion: {
        questionTitle: "",
        questionText: "",
        possibleAnswers: [],
        image: ""
      },
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0
    };
  },
  methods: {
    async answerClickedHandler() {
      //TODO ajouter de la vérification du résultat depuis le signal émis
      this.currentQuestionPosition++;
      if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
        this.endQuiz();
      } else {
        this.loadQuestionByPosition()
      }
    },
    endQuiz() {
      //TODO Ajouter fin quizz
    },
    async loadQuestionByPosition() {
      const question = await QuizApiService.getQuestion(this.currentQuestionPosition).data
      this.currentQuestion.questionText = question.text;
      this.currentQuestion.questionTitle = question.title;
      this.currentQuestion.image = question.image;
      this.currentQuestion.possibleAnswers = question.possibleAnswers;
    }
  }
}
</script>
