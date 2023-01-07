import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomePage",
      component: () => import("@/views/frontoffice/HomePage.vue"),
    },
    {
      path: "/start-new-quiz",
      name: "NewQuizPage",
      component: () => import("@/views/frontoffice/NewQuizPage.vue"),
    },
    {
      path: "/questions",
      name: "QuestionsPage",
      component: () => import("@/views/frontoffice/QuestionManager.vue"),
    },
    {
      path: "/administration",
      name: "AdministrationPage",
      component: () => import("@/views/backoffice/AdministrationPage.vue"),
    },
    {
      path: "/login",
      name: "LoginPage",
      component: () => import("@/views/frontoffice/LoginPage.vue"),
    },
    {
      path: "/score",
      name: "ScorePage",
      component: () => import("@/views/frontoffice/ScorePage.vue"),
    },
  ],
});

export default router;
