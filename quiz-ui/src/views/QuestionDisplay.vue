<template>
    <h2><b>{{ question.title }}</b></h2>
    <p>{{ question.text }}</p>
    <img :src="'data:image/jpeg;charset=utf-8;base64,'+question.image" />
    <v-btn block v-for="(answer,index) in question.possibleAnswers" :key="answer" @click="$emit('answer-selected', index+1)">{{answer.text}}</v-btn>
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