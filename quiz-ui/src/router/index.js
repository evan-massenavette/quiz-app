import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: () => import('@/views/HomePage.vue')
    },
    {
      path: '/start-new-quiz',
      name: 'NewQuizPage',
      component: () => import('@/views/NewQuizPage.vue')
    },
    {
      path: '/questions',
      name: 'QuestionsPage',
      component: () => import('@/views/QuestionManager.vue')
    },
    {
      path: '/administration',
      name: 'AdministrationPage',
      component: () => import('@/views/AdministrationPage.vue')
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: () => import('@/views/LoginPage.vue')
    },
    {
      path: '/score',
      name: 'ScorePage',
      component: () => import('@/views/ScorePage.vue')
    }
  ]
})

export default router
