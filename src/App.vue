<template>
  <v-app id="app">
    <app-menu />

    <v-main>
      <router-view></router-view>
    </v-main>
    <app-footer />
  </v-app>
</template>

<script>
import AppMenu from "./components/AppMenu.vue";
import AppFooter from "./components/AppFooter.vue";

export default {
  name: "App",
  components: {
    "app-menu": AppMenu,
    "app-footer": AppFooter,
  },
  data: () => ({
    //
  }),
  computed: {},
};
</script>
