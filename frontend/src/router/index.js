import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import InferencePage from '../components/InferencePage.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/inference', 
    name: 'InferencePage',
    component: InferencePage,
  },
  
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;