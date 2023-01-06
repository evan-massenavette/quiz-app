<template>
  <div :keys="questions" v-for="(question,index) in questions">
    <QuestionEditor :question="question" :loading="loading"/>
    <v-btn :disabled="loading || !canGoUp(index)" @click="goUp(index)" icon="mdi-arrow-collapse-up"></v-btn>
    <v-btn :disabled="loading || !canGoDown(index)" @click="goDown(index)" icon="mdi-arrow-collapse-down"></v-btn>
    <v-btn :disabled="loading" @click="deleteAt(index)" icon="mdi-close"></v-btn>
  </div>
</template>
<script>
import QuizApiService from '@/services/QuizApiService'
import StorageService from '@/services/StorageService'
import QuestionEditor from './QuestionEditor.vue'
export default {
  async created() {
    this.loading=true
    await this.loadQuestions()
    this.token = StorageService.getToken()
    this.loading=false
  },
  data() {
      return {
          questions: [],
          size: 0,
          loading: false,
          token: ""
      };
  },
  components: { QuestionEditor },
  methods:{
    async loadQuestions(){
      this.questions=[]
      try {
          const quizInfoRequest = await QuizApiService.getQuizInfo();
          this.size = quizInfoRequest.data.size;
          for (let i = 1; i <= this.size; i++) {
              let questionRequest = await QuizApiService.getQuestion(i);
              let question = questionRequest.data;
              this.questions[i-1]=question;
          }
          console.log(this.questions);
      }
      catch (e) {
          console.error(e);
      }
    },
    async changePosition(index, offset){
      this.loading=true
      try{
        const id = this.questions[index].id
        const question = this.questions[index]
        question.position += offset
        await QuizApiService.modifyQuestion(this.token,id,question.text,question.title,question.image,question.position,question.possibleAnswers)
      } catch (e) {
        console.error(e)
      }
      await this.loadQuestions()
      this.loading=false 
    },
    canGoUp(index){
      return index>0
    },
    async goUp(index){
      await this.changePosition(index,-1)
    },
    canGoDown(index){
      return index<this.size-1
    },
    async goDown(index){
      await this.changePosition(index,1)
    },
    async deleteAt(index){
      this.loading=true
      try{
        await QuizApiService.deleteQuestion(this.token,this.questions[index].id)
      } catch (e) {
        console.error(e)
      }
      await this.loadQuestions()
      this.loading=false
    }
  }
}
</script>
