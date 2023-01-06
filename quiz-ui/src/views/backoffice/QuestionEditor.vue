<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-form v-model="form" @submit.prevent="$emit('edited',question)">
        <v-card-title>
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Title" clearable placeholder="Enter the title"
            :rules="[required]" :disabled="loading" v-model="question.title" />
        </v-card-title>

        <v-card-text>
          <img :src="question.image"/>
          <ImageUpload @file-change="imageFileChangedHandler"/>
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Text" clearable placeholder="Enter the text"
            :rules="[required]" :disabled="loading" v-model="question.text" />
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Answer 1" clearable placeholder="Enter the answer"
            :rules="[required]" :disabled="loading" v-model="question.possibleAnswers[0].text" />
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Answer 2" clearable placeholder="Enter the answer"
            :rules="[required]" :disabled="loading" v-model="question.possibleAnswers[1].text" />
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Answer 3" clearable placeholder="Enter the answer"
            :rules="[required]" :disabled="loading" v-model="question.possibleAnswers[2].text" />
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Answer 4" clearable placeholder="Enter the answer"
            :rules="[required]" :disabled="loading" v-model="question.possibleAnswers[3].text" />
          <v-btn-toggle v-model="goodAnswer" divided mandatory>
            <v-btn @click="changeGoodAnswer">1</v-btn>
            <v-btn @click="changeGoodAnswer">2</v-btn>
            <v-btn @click="changeGoodAnswer">3</v-btn>
            <v-btn @click="changeGoodAnswer">4</v-btn>
          </v-btn-toggle>
        </v-card-text>
        <v-card-actions>
          <v-btn :disabled="loading || (!form && !existent) " :loading="loading" type="submit">Edit</v-btn>
          <v-btn v-if="existent" :disabled="loading || !canGoUp" @click="$emit('go-up',question)" icon="mdi-arrow-collapse-up"></v-btn>
          <v-btn v-if="existent" :disabled="loading || !canGoDown" @click="$emit('go-down',question)" icon="mdi-arrow-collapse-down"></v-btn>
          <v-btn v-if="existent" :disabled="loading" @click="$emit('deleted',question)" icon="mdi-close"></v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>
<script>
import ImageUpload from './ImageUpload.vue';
export default {
  components: { ImageUpload },
    props: {
        currentQuestion: {
            type: Object
        },
        loading: {
            type: Boolean
        },
        existent: {
            type: Boolean
        },
        canGoUp: {
            type: Boolean
        },
        canGoDown: {
            type: Boolean
        }
    },
    data(){
      return{
        form: this.existent,
        question: this.currentQuestion || {title:"",image:"",text:"",possibleAnswers:[{text:"",isCorrect:true},{text:"",isCorrect:false},{text:"",isCorrect:false},{text:"",isCorrect:false}]},
        goodAnswer: this.currentQuestion.possibleAnswers.findIndex((obj)=>obj.isCorrect===true)
      }
    },
    methods:{
      changeGoodAnswer(){
        for(let i=0;i<4;i++){
          this.question.possibleAnswers[i].isCorrect = i===this.goodAnswer
        }
      },
      required(v){
        return !!v || 'Required'
      },
      imageFileChangedHandler(b64String) {
        this.question.image = b64String;
      }
    },
    emits: ["edited","go-up","go-down","deleted"]
}
</script>
