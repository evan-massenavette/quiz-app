<template>
  <v-container class="pa-0">
    <v-form v-model="form" @submit.prevent="$emit('edited', question)" class="my-5">

      <v-container>

        <v-card-title class="pa-0 ma-0">
          <v-text-field prepend-icon="mdi-format-size" type="text" label="Question Title" clearable
            placeholder="Enter the title" :rules="[required]" :disabled="loading" v-model="question.title" />
        </v-card-title>

        <v-img :src="question.image" :class="question.image ? 'ma-auto mb-5' : 'd-none'" style="height: 200px;" />
        <ImageUpload @file-change="imageFileChangedHandler" />

        <v-text-field prepend-icon="mdi-help" type="text" label="Question" clearable placeholder="Enter the text"
          :rules="[required]" :disabled="loading" v-model="question.text" />
        <v-text-field prepend-icon="mdi-lightbulb-on-outline" type="text" label="Answer 1" clearable
          placeholder="Enter the answer" :rules="[required]" :disabled="loading"
          v-model="question.possibleAnswers[0].text" />
        <v-text-field prepend-icon="mdi-lightbulb-on-outline" type="text" label="Answer 2" clearable
          placeholder="Enter the answer" :rules="[required]" :disabled="loading"
          v-model="question.possibleAnswers[1].text" />
        <v-text-field prepend-icon="mdi-lightbulb-on-outline" type="text" label="Answer 3" clearable
          placeholder="Enter the answer" :rules="[required]" :disabled="loading"
          v-model="question.possibleAnswers[2].text" />
        <v-text-field prepend-icon="mdi-lightbulb-on-outline" type="text" label="Answer 4" clearable
          placeholder="Enter the answer" :rules="[required]" :disabled="loading"
          v-model="question.possibleAnswers[3].text" />

        <div id="controls_container" class="d-flex flex-row justify-center">

          <div class="d-flex align-center mr-4">
            <p>Correct answer</p>
          </div>
          <v-btn-toggle v-model="goodAnswer" divided mandatory id="good_answer_selector" class="controls_subcontainer">
            <v-btn @click="changeGoodAnswer">1</v-btn>
            <v-btn @click="changeGoodAnswer">2</v-btn>
            <v-btn @click="changeGoodAnswer">3</v-btn>
            <v-btn @click="changeGoodAnswer">4</v-btn>
          </v-btn-toggle>

          <v-spacer />

          <v-card-actions class="controls_subcontainer">
            <v-btn :disabled="loading || (!form && !existent)" :loading="loading" type="submit" color="accent">{{
              existent? "Edit": "Add"
            }}</v-btn>

            <v-btn v-if="existent" :disabled="loading || !canGoUp" @click="$emit('go-up', question)"
              icon="mdi-arrow-collapse-up"></v-btn>
            <v-btn v-if="existent" :disabled="loading || !canGoDown" @click="$emit('go-down', question)"
              icon="mdi-arrow-collapse-down"></v-btn>
            <v-btn v-if="existent" :disabled="loading" @click="$emit('deleted', question)" icon="mdi-close"></v-btn>
          </v-card-actions>

        </div>

      </v-container>

    </v-form>

    <v-divider />

  </v-container>
</template>

<style scoped>
#controls_container {
  height: 60px;
}

.controls_subcontainer {
  height: 100%;
}

#good_answer_selector {
  border: 1px solid rgb(var(--v-theme-surface-lighten-1))
}
</style>

<script>
import ImageUpload from '@/views/backoffice/ImageUpload.vue';

export default {
  components: { ImageUpload },
  props: {
    currentQuestion: {
      type: Object,
      required: true
    },
    loading: {
      type: Boolean,
      required: true
    },
    existent: {
      type: Boolean,
      required: true
    },
    canGoUp: {
      type: Boolean
    },
    canGoDown: {
      type: Boolean
    }
  },
  data() {
    return {
      form: this.existent,
      question: this.currentQuestion,
      goodAnswer: this.currentQuestion.possibleAnswers.findIndex((obj) => obj.isCorrect === true),
    };
  },
  methods: {
    required(v) {
      return !!v || 'Required'
    },
    imageFileChangedHandler(b64String) {
      this.question.image = b64String;
      console.log('this.question.image = ', this.question.image)
    },
    changeGoodAnswer() {
      for (let i = 0; i < 4; i++) {
        this.question.possibleAnswers[i].isCorrect = i === this.goodAnswer
      }
    },
  },
  emits: ["edited", "go-up", "go-down", "deleted"]
}
</script>
