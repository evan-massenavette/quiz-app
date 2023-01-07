<template>
  <h2>
    <b>{{ question.title }}</b>
  </h2>
  <img :src="question.image" style="height: 200px" />
  <p>{{ question.text }}</p>
  <v-btn
    class="answer-btn"
    height="4em"
    color="accent"
    :key="answer"
    v-for="(answer, index) in question.possibleAnswers"
    :disabled="loading || index + 1 === currentAnswer"
    @click="$emit('answer-selected', index + 1)"
    block
    >{{ answer.text }}</v-btn
  >
</template>
<style scoped>
.answer-btn {
  margin-top: 1em;
}
</style>
<script>
export default {
  props: {
    question: {
      type: Object,
    },
    currentAnswer: {
      type: [Number, undefined],
    },
    loading: {
      type: Boolean,
    },
  },
  emits: ["answer-selected"],
};
</script>
