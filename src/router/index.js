import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Posts from '../views/Posts.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Posts
  },
  {
    path: '/about',
    name: 'About Mason',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/donate',
    name: 'Donate',
    component: () => import(/* webpackChunkName: "donate" */ '../views/Donate.vue')
  },
  // {
  //   path: '/posts',
  //   name: 'Posts',
  //   component: () => import(/* webpackChunkName: "posts" */ '../views/Posts.vue')
  // }
]

const router = new VueRouter({
  routes
})

export default router
