import { createRouter, createWebHistory } from 'vue-router';
import {useAuthStore} from '@/store'
import LoginView from '../views/LoginView.vue';
import ForgotPassView from '../views/ForgotPassView.vue';
import NotFoundView from '../views/NotFoundView.vue';
import UserProfile from '../components/Users/UserProfile.vue';
import UserRegister from '../components/Users/RegisterUser.vue';
import DashboardView from '../views/DashboardView.vue';

const routes = [
  // Ruta por defecto que apunta a LoginView
  { path: '/', name: 'Login', component: LoginView },
  // Otras rutas
  { path: '/forgot-password', name: 'ForgotPass', component: ForgotPassView },
  { path: '/not-found', name: 'NotFound', component: NotFoundView },
  { path: '/user-profile', name: 'UserProfile', component: UserProfile },
  { path: '/user-register', name: 'UserRegister', component: UserRegister },
  { path: '/dashboard', name: 'Dashboard', component: DashboardView },

  // Redirección en caso de ruta no encontrada
  { path: '/:pathMatch(.*)*', redirect: '/not-found' },
];

const router = createRouter({
  history: createWebHistory(process.env.VITE_BASE_URL),
  routes,
});

export default router;