<template>
  <div :key="question.position" v-for="question in questions">
    <QuestionEditor :currentQuestion="question" :loading="loading" :existent="true" :canGoUp="canGoUpQuestion(question)"
      :canGoDown="canGoDownQuestion(question)" @edited="modifyQuestion" @go-up="goUpQuestion" @go-down="goDownQuestion"
      @deleted="deleteQuestion" />
  </div>
  <v-btn v-if="!isAdding" :disabled="loading" icon="mdi-plus" @click="isAdding = true"></v-btn>
  <QuestionEditor v-else :loading="loading" :existent="false" @edited="addQuestion" :currentQuestion="emptyQuestion" />
</template>

<script>
import QuizApiService from '@/services/QuizApiService'
import StorageService from '@/services/StorageService'
import QuestionEditor from './QuestionEditor.vue'

export default {
  async created() {
    this.loading = true
    await this.loadQuestions()
    this.token = StorageService.getToken()
    this.loading = false
  },
  data() {
    return {
      questions: [],
      size: 0,
      emptyQuestion: { title: "", image: "", text: "", possibleAnswers: [{ text: "", isCorrect: true }, { text: "", isCorrect: false }, { text: "", isCorrect: false }, { text: "", isCorrect: false }] },
      loading: false,
      token: "",
      isAdding: false
    };
  },
  components: { QuestionEditor },
  methods: {
    async loadQuestions() {
      this.questions = []
      try {
        const questionsRequest = await QuizApiService.getAllQuestions()
        this.questions = questionsRequest.data
        this.size = this.questions.length
      }
      catch (e) {
        console.error(e);
      }
    },
    async changePosition(question, offset) {
      try {
        question.position += offset
        await QuizApiService.modifyQuestion(this.token, question.id, question.text, question.title, question.image, question.position, question.possibleAnswers)
      } catch (e) {
        console.error(e)
      }
      await this.loadQuestions()
    },
    async goUpQuestion(question) {
      this.loading = true
      await this.changePosition(question, -1)
      this.loading = false
    },
    async goDownQuestion(question) {
      this.loading = true
      await this.changePosition(question, 1)
      this.loading = false
    },
    async deleteQuestion(question) {
      this.loading = true
      try {
        await QuizApiService.deleteQuestion(this.token, question.id)
      } catch (e) {
        console.error(e)
      }
      await this.loadQuestions()
      this.loading = false
    },
    async modifyQuestion(question) {
      this.loading = true
      try {
        await QuizApiService.modifyQuestion(this.token, question.id, question.text, question.title, question.image, question.position, question.possibleAnswers)
      } catch (e) {
        console.error(e)
      }
      await this.loadQuestions()
      this.loading = false
    },
    async addQuestion(question) {
      this.loading = true
      try {
        await QuizApiService.addQuestion(this.token, question.text, question.title, question.image, ++this.size, question.possibleAnswers)
      } catch (e) {
        console.error(e)
      }
      await this.loadQuestions()
      this.isAdding = false
      this.loading = false
    },
    canGoUpQuestion(question) {
      return question.position - 1 > 0
    },
    canGoDownQuestion(question) {
      return question.position < this.size
    },
  }
}
</script>
