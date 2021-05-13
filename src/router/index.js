import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about/mason",
    name: "Our Story",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutMason.vue"),
  },
  {
    path: "/about/austin",
    name: "Our Story",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutAustin.vue"),
  },
  {
    path: "/about/hlh",
    name: "Our Story",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutHlh.vue"),
  },
  {
    path: "/about/xlp2",
    name: "Our Story",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutXlp2.vue"),
  },
  {
    path: "/about",
    name: "Our Story",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/donate",
    name: "Donate",
    component: () =>
      import(/* webpackChunkName: "donate" */ "../views/Donate.vue"),
  },
  {
    path: "/posts",
    name: "Posts",
    component: () =>
      import(/* webpackChunkName: "posts" */ "../views/Posts.vue"),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
