<template>
  <div class="about pa-5">
    <v-row justify="space-around">
      <v-col cols="12" sm="10" md="6" lg="6" xl="6">
        <mason-bio />
      </v-col>
      <v-col cols="10" md="6" lg="6" xl="6">
        <carousel-card :images="images" />
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
  data: () => ({
    images: [
      "mason-1.jpeg",
      "mason-2.jpeg",
      "mason-3.jpeg",
      "mason-4.jpeg",
      "mason-5.jpeg",
      "mason-6.jpeg",
      "mason-7.jpeg",
      "mason-8.jpeg",
      "mason-9.jpeg",
      "mason-10.jpeg",
      "mason-11.jpeg",
      "mason-14.jpeg",
      "mason-15.jpeg",
      "mason-16.jpeg",
      "mason-17.jpeg",
    ],
  }),
  mounted() {},
  methods: {},
};
</script>
