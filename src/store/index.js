import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import allPosts from './json/posts.json'

export default new Vuex.Store({
  state: {
    posts: allPosts,
    pfp: 'pfp.jpeg',
    items: [
      { title: 'Home', icon: 'mdi-home', to: '/' },
      { title: 'Posts', icon: 'mdi-facebook', to: '/posts' },
      { title: 'About Mason', icon: 'mdi-information-outline', to: '/about/mason' },
      { title: 'About Austin', icon: 'mdi-information-outline', to: '/about/austin' },
      { title: 'Donate', icon: 'mdi-emoticon-happy-outline', to: '/donate' },

    ],
    links: [
      {
        title: 'Facebook',
        icon: 'mdi-facebook',
        url: 'https://www.facebook.com/Hope-for-Spencer-Boys-623432097701465/'
      },
      {
        title: 'Cota',
        icon: 'mdi-facebook',
        url: 'https://cotaforteamspencer.com'
      },
      {
        title: 'Donate',
        icon: 'mdi-emoticon-happy-outline',
        url: 'https://ilprairiecf.org/mason-spencer-lives-on-fund'
      }
    ],
    drawer: true,
  },
  getters: {
    items(state) {
      return state.items
    },
    drawer(state) {
      return state.drawer
    },
    links(state) {
      return state.links
    },
    pfp(state) {
      return state.pfp
    },
    posts(state) {
      return state.posts
    }
  },
  mutations: {
    drawer(state, val) {
      state.drawer = val
    },
  },
  actions: {
  },
  modules: {
  }
})
