import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items: [
      { title: 'Home', icon: 'mdi-home', to: '/' },
      { title: 'About Mason', icon: 'mdi-information-outline', to: '/about' },
      { title: 'Donate', icon: 'mdi-emoticon-happy-outline', to: '/donate' }
    ],
    drawer: false,
  },
  getters: {
    items(state) {
      return state.items
    },
    drawer(state) {
      return state.drawer
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
