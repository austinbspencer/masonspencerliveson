import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items: [
      { title: 'Home', icon: 'mdi-home', to: '/' },
      { title: 'Posts', icon: 'mdi-facebook', to: '/posts' },
      { title: 'About Mason', icon: 'mdi-information-outline', to: '/about' },
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
        url: 'cotaforteamspencer.com'
      }
    ],
    drawer: false,
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
