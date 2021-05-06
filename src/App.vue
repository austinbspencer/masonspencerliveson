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

<style>
h1 {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 32px;
  font-style: normal;
  font-variant: normal;
  font-weight: bold;
  line-height: 36px;
}
h2 {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 28px;
  font-style: normal;
  font-variant: normal;
  font-weight: bold;
  line-height: 30px;
}
h3 {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 24px;
  font-style: normal;
  font-variant: normal;
  font-weight: bold;
  line-height: 26px;
}
h4 {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 20px;
  font-style: normal;
  font-variant: normal;
  font-weight: bold;
  line-height: 22px;
}
p {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 14px;
  font-style: normal;
  font-variant: normal;
  font-weight: 400;
  line-height: 20px;
}
blockquote {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 21px;
  font-style: normal;
  font-variant: normal;
  font-weight: 400;
  line-height: 30px;
}
pre {
  font-family: TimesNewRoman, "Times New Roman", Times, Baskerville, Georgia,
    serif;
  font-size: 13px;
  font-style: normal;
  font-variant: normal;
  font-weight: 400;
  line-height: 18px;
}
</style>
