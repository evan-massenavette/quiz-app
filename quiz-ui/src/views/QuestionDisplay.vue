<template>
    <h1>{{ question.questionTitle }}</h1>
    <p>{{ question.questionText }}</p>
    <img v-if="question.image" :src="question.image" />
    <!--a v-for="(answer,index) in question.possibleAnswers" :key="answer" @click="$emit('answer-selected', index)">{{answer.text}}</a-->
</template>
<script>
export default {
    props: {
        question: {
            type: Object
        }
    },
    emits: ["answer-selected"]
}
</script>