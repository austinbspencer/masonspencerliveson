<template>
  <div class="about pa-5">
    <v-row justify="space-around">
      <v-col cols="12" sm="10" md="6" lg="6" xl="6">
        <austin-bio />
      </v-col>
      <v-col cols="10" md="6" lg="6" xl="6">
        <carousel-card :images="images" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import AustinBio from "../components/About/AustinBio.vue";
import CarouselCard from "../components/About/Carousel.vue";

export default {
  name: "Aboutaustin",
  components: {
    "austin-bio": AustinBio,
    "carousel-card": CarouselCard,
  },
  directives: {},
  data() {
    return {
      images: ["austin-1.jpg", "austin-2.jpg"],
    };
  },
  mounted() {},
  methods: {},
};
</script>

<style lang="scss" scoped></style>
