<template>
  <v-container>
    <v-card class="mx-auto my-12">
      <v-form v-model="form" @submit.prevent="modified">
        <v-card-title>
          <v-text-field prepend-icon="mdi-form-textbox" type="text" label="Title" clearable placeholder="Enter the title"
            :rules="[required]" :disabled="loading" v-model="question.title" />
        </v-card-title>
        <v-card-text>
          <!-- IMAGE A METTRE ICI -->
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
        </v-card-text>
        <v-card-actions>
          <v-btn :disabled="loading || !form" :loading="loading" type="submit">Edit</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>
<script>
export default {
    props: {
        question: {
            type: Object
        },
        loading: {
            type: Boolean
        }
    },
    data(){
      return{
        form: false,
      }
    },
    methods:{
      required(){
        return !!v || 'Required'
      }
    },
    emits: ["modified"]
}
</script>
