<template>
    <h2><b>{{ question.title }}</b></h2>
    <p>{{ question.text }}</p>
    <img :src="question.image" />
    <a v-for="(answer,index) in question.possibleAnswers" :key="answer" @click="$emit('answer-selected', index+1)">{{answer.text}}</a>
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