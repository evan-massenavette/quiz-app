<template>
    <h2><b>{{ question.title }}</b></h2>
    <p>{{ question.text }}</p>
    <img :src="'data:image/jpeg;charset=utf-8;base64,'+question.image" />
    <v-btn :key="answer" v-for="(answer,index) in question.possibleAnswers" :disabled="loading || index+1===currentAnswer" @click="$emit('answer-selected', index+1)" block>{{answer.text}}</v-btn>
</template>
<script>
export default {
    props: {
        question: {
            type: Object
        },
        currentAnswer: {
            type: [Number,undefined]
        },
        loading: {
            type: Boolean
        }
    },
    emits: ["answer-selected"]
}
</script>