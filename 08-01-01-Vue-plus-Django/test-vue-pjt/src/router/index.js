import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import ProductView from '@/views/ProductView.vue'
import MapView from '@/views/MapView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
// import UserView from '@/views/UserView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    // {
    //   path: '/user/:id',
    //   name: 'user',
    //   component: UserView
    // },
  ]
})

export default router
