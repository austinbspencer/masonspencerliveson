<template>
  <div>
    <v-tabs v-model="tab" align-with-title light>
      <v-tabs-slider color="yellow"></v-tabs-slider>

      <v-tab v-for="item in information" :key="item.title">
        {{ item.title }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <AboutInfo />
      </v-tab-item>
      <v-tab-item>
        <Mason />
      </v-tab-item>
      <v-tab-item>
        <Austin />
      </v-tab-item>
      <v-tab-item>
        <Hlh />
      </v-tab-item>
      <v-tab-item>
        <Xlp />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import AboutInfo from "../components/About/About.vue";
import Mason from "../views/AboutMason.vue";
import Austin from "../views/AboutAustin.vue";
import Hlh from "../views/AboutHlh.vue";
import Xlp from "../views/AboutXlp2.vue";
export default {
  name: "About",
  components: {
    AboutInfo,
    Mason,
    Austin,
    Hlh,
    Xlp,
  },
  directives: {},
  data() {
    return {
      tab: null,
    };
  },
  computed: {
    information() {
      return this.$store.getters.information;
    },
  },
  mounted() {
    this.$store.commit("drawer", false);
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
