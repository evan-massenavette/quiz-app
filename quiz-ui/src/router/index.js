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
      path: '/start-new-quiz-page',
      name: 'NewQuizPage',
      component: () => import('@/views/NewQuizPage.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/questions',
      name: 'Questions',
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
    }
  ]
})

export default router
