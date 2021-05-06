<template>
  <div class="about pa-5">
    <v-row justify="space-around">
      <v-col
        cols="12"
        sm="10"
        md="6"
        lg="6"
        xl="6"
      >
        <mason-bio />
      </v-col>
      <v-col
        cols="10"
        md="6"
        lg="6"
        xl="6"
      >
        <carousel-card />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import MasonBio from "../components/About/MasonBio.vue";
import CarouselCard from "../components/About/Carousel.vue";

export default {
  name: "About",
  components: {
    "mason-bio": MasonBio,
    "carousel-card": CarouselCard,
  },
  directives: {},
  data: () => ({}),
  mounted() {
    this.$store.commit("drawer", false);
  },
  methods: {},
};
</script>